#!/bin/bash
# fetch_verify.sh — rebuild-manifest executor (#69, 2026-08-06/07 night).
# Makes the paper's §3/§4 claim EXECUTABLE: "every input is hash-pinned …
# every number replays from hash-pinned inputs" must stay testable after the
# regenerable bulk (models/, lexical_resources/, nltk_data/, data/ payloads,
# vectors/) leaves the working tree.
#
# Reads the sibling rebuild_manifest.tsv (tab-separated, one row per FETCHABLE
# artifact — the unit a stranger downloads, not the files it expands into):
#   artifact_id  method  source  version  sha256  local_path  notes
#     method ∈ curl | hf (huggingface snapshot) | gensim | nltk | manual
#     sha256      hash of the FETCHED UNIT (archive/file), or DIR:<n>@<h>
#                 for hash-of-sorted-file-hashes over an expanded tree
#     manual      rows are listed and skipped with instructions (paywalled /
#                 form-gated sources; the manifest still records the pin)
#
# Modes:
#   --list            print the manifest as parsed (default when no flag)
#   --verify-local    hash what is ON DISK now at local_path, compare to pin
#                     (no network; the tonight-mode check)
#   --fetch DIR       download each artifact into DIR/<artifact_id>/ and
#                     verify against the pin (the stranger-mode check)
# Never touches local_path contents; never deletes; never executes fetched
# code. Exits nonzero if any row fails, with a per-row PASS/FAIL table
# (notify_sound doctrine: fail loud, never silently).
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
MANIFEST="$HERE/rebuild_manifest.tsv"
REPO="$HERE"
MODE="${1:---list}"
DEST="${2:-}"

[ -r "$MANIFEST" ] || { echo "fetch_verify: manifest missing: $MANIFEST"; exit 2; }

hash_file() { shasum -a 256 "$1" 2>/dev/null | awk '{print $1}'; }
hash_tree() { # deterministic dir pin: sha256 of sorted per-file sha256 list.
  # find -L: symlinked payloads count as their targets (a hash-perfect tree
  # staged via symlinks must verify identically to a fetched one — the 0812
  # battery caught LaBSE reporting FAIL with a matching hash because the
  # count refused to traverse what the hash traversed; #71).
  ( cd "$1" 2>/dev/null && find -L . -type f -not -name '.DS_Store' -print0 \
      | sort -z | xargs -0 shasum -a 256 2>/dev/null | awk '{print $1"  "$2}' \
      | shasum -a 256 | awk '{print $1}' )
}

FAIL=0; ROW=0
printf '%-28s %-8s %-10s %s\n' 'artifact' 'method' 'verdict' 'detail'
while IFS=$'\t' read -r ID METHOD SOURCE VERSION SHA LOCAL NOTES; do
  case "$ID" in ''|'#'*|artifact_id) continue;; esac
  ROW=$((ROW+1))
  case "$MODE" in
    --list)
      printf '%-28s %-8s %-10s %s\n' "$ID" "$METHOD" "$VERSION" "$SOURCE";;
    --verify-local)
      P="$REPO/$LOCAL"
      if [ ! -e "$P" ]; then
        printf '%-28s %-8s %-10s %s\n' "$ID" "$METHOD" 'ABSENT' "$LOCAL"; FAIL=1
      else
        case "$SHA" in
          DIR:*) GOT="DIR:$(find -L "$P" -type f -not -name '.DS_Store' | wc -l | tr -d ' ')@$(hash_tree "$P")";;
          *)     GOT="$(hash_file "$P")";;
        esac
        if [ "$GOT" = "$SHA" ]; then
          printf '%-28s %-8s %-10s %s\n' "$ID" "$METHOD" 'PASS' "$LOCAL"
        else
          printf '%-28s %-8s %-10s %s\n' "$ID" "$METHOD" 'FAIL' "pin=$SHA got=$GOT"; FAIL=1
        fi
      fi;;
    --fetch)
      [ -n "$DEST" ] || { echo 'fetch_verify: --fetch needs a DIR'; exit 2; }
      OUT="$DEST/$ID"; mkdir -p "$OUT"
      case "$METHOD" in
        curl)   curl -L --fail -o "$OUT/$(basename "$SOURCE")" "$SOURCE" || { printf '%-28s %-8s %-10s %s\n' "$ID" "$METHOD" 'FETCHFAIL' "$SOURCE"; FAIL=1; continue; }
                GOT="$(hash_file "$OUT/$(basename "$SOURCE")")";;
        hf)     python3 -c "from huggingface_hub import snapshot_download; snapshot_download('$SOURCE', revision='$VERSION', local_dir='$OUT')" || { printf '%-28s %-8s %-10s %s\n' "$ID" "$METHOD" 'FETCHFAIL' "$SOURCE"; FAIL=1; continue; }
                GOT="DIR:$(find "$OUT" -type f -not -name '.DS_Store' | wc -l | tr -d ' ')@$(hash_tree "$OUT")";;
        nltk)   python3 -c "import nltk; nltk.download('$SOURCE', download_dir='$OUT')" || { printf '%-28s %-8s %-10s %s\n' "$ID" "$METHOD" 'FETCHFAIL' "$SOURCE"; FAIL=1; continue; }
                GOT="DIR:$(find "$OUT" -type f -not -name '.DS_Store' | wc -l | tr -d ' ')@$(hash_tree "$OUT")";;
        gensim) # --fetch must hash the SAME UNIT the pin covers. This row's pin is
                # a file hash over local_path (…/vectors/glove-wiki-gigaword-50.txt
                # — manifest notes: "file-hash identity pin"), and REBUILD.md
                # records --verify-local 61/61 PASS on a full tree, i.e. the pin
                # equals sha256 of that DECOMPRESSED .txt. gensim-data caches the
                # artifact as a .gz, so hashing the cache file itself could never
                # equal the pin — which is what the previous line did, except it
                # did not even hash: it assigned a literal placeholder string, so
                # this row could never PASS via --fetch under any circumstances.
                # Decompress the cached .gz to <artifact_id>.txt and hash that.
                # ⚠ UNTESTED-BY-RUN (#71, 2026-08-12): exercising this needs the
                # network and the gensim package, neither available where the fix
                # was written. If the committed .txt was produced with any extra
                # post-processing, this row now FAILS LOUD with pin=/got= — the
                # correct outcome, and strictly better than a placeholder that
                # silently guaranteed failure.
                GPATH="$(python3 -c "import gensim.downloader as g; print(g.load('$SOURCE', return_path=True))")" \
                  || { printf '%-28s %-8s %-10s %s\n' "$ID" "$METHOD" 'FETCHFAIL' "$SOURCE"; FAIL=1; continue; }
                [ -n "$GPATH" ] && [ -r "$GPATH" ] \
                  || { printf '%-28s %-8s %-10s %s\n' "$ID" "$METHOD" 'FETCHFAIL' "gensim returned no readable path: ${GPATH:-<empty>}"; FAIL=1; continue; }
                case "$GPATH" in
                  *.gz) gunzip -c "$GPATH" > "$OUT/$ID.txt" \
                          || { printf '%-28s %-8s %-10s %s\n' "$ID" "$METHOD" 'FETCHFAIL' "gunzip failed: $GPATH"; FAIL=1; continue; }
                        GOT="$(hash_file "$OUT/$ID.txt")";;
                  *)    GOT="$(hash_file "$GPATH")";;
                esac;;
        manual) printf '%-28s %-8s %-10s %s\n' "$ID" "$METHOD" 'MANUAL' "$NOTES"; continue;;
        *)      printf '%-28s %-8s %-10s %s\n' "$ID" "$METHOD" 'BADMETHOD' ''; FAIL=1; continue;;
      esac
      if [ "$GOT" = "$SHA" ]; then printf '%-28s %-8s %-10s %s\n' "$ID" "$METHOD" 'PASS' ''
      else printf '%-28s %-8s %-10s %s\n' "$ID" "$METHOD" 'FAIL' "pin=$SHA got=$GOT"; FAIL=1; fi;;
  esac
done < "$MANIFEST"
[ "$ROW" -gt 0 ] || { echo 'fetch_verify: zero data rows in manifest'; exit 2; }
exit $FAIL
