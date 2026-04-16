#!/usr/bin/env bash
# IndexNow submission script for loyalandloved.co.uk
# Run after every git push + Cloudflare cache purge to notify
# search engines (Bing, Yandex, Naver, Seznam, Amazon, Yep)
# that content has changed.
#
# Usage:
#   ./scripts/indexnow-submit.sh                    # submit all URLs from sitemap
#   ./scripts/indexnow-submit.sh https://loyalandloved.co.uk/articles/new-article.html  # submit one URL
#
# You only need to submit to ONE endpoint — it shares with all
# participating engines automatically.

set -euo pipefail

HOST="loyalandloved.co.uk"
KEY="4f7b6695f5654be0918b411b1f7494d2"
ENDPOINT="https://api.indexnow.org/indexnow"

if [ $# -gt 0 ]; then
  # Single URL mode
  URL="$1"
  echo "Submitting single URL: ${URL}"
  HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" \
    "${ENDPOINT}?url=$(python3 -c "import urllib.parse; print(urllib.parse.quote('${URL}', safe=''))")&key=${KEY}")
  echo "Response: HTTP ${HTTP_CODE}"
  if [ "${HTTP_CODE}" = "200" ] || [ "${HTTP_CODE}" = "202" ]; then
    echo "OK — accepted by IndexNow."
  else
    echo "WARNING — unexpected response. Check https://www.indexnow.org/faq for error codes."
  fi
  exit 0
fi

# Bulk mode — pull all URLs from sitemap.xml
echo "Fetching sitemap from https://${HOST}/sitemap.xml ..."
URLS=$(curl -s "https://${HOST}/sitemap.xml" \
  | grep -oP '(?<=<loc>)[^<]+' \
  | head -100)

if [ -z "${URLS}" ]; then
  echo "ERROR: No URLs found in sitemap. Check https://${HOST}/sitemap.xml"
  exit 1
fi

COUNT=$(echo "${URLS}" | wc -l)
echo "Found ${COUNT} URLs. Submitting to IndexNow..."

# Build JSON payload for bulk POST
URL_LIST=$(echo "${URLS}" | python3 -c "
import sys, json
urls = [line.strip() for line in sys.stdin if line.strip()]
print(json.dumps(urls))
")

PAYLOAD=$(cat <<ENDJSON
{
  "host": "${HOST}",
  "key": "${KEY}",
  "urlList": ${URL_LIST}
}
ENDJSON
)

HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" \
  -X POST "${ENDPOINT}" \
  -H "Content-Type: application/json; charset=utf-8" \
  -d "${PAYLOAD}")

echo "Response: HTTP ${HTTP_CODE}"
if [ "${HTTP_CODE}" = "200" ] || [ "${HTTP_CODE}" = "202" ]; then
  echo "OK — ${COUNT} URLs submitted to IndexNow (shared with Bing, Yandex, Naver, Seznam, Amazon, Yep)."
else
  echo "WARNING — unexpected response code ${HTTP_CODE}."
  echo "Common issues:"
  echo "  422 = key file not accessible at https://${HOST}/${KEY}.txt"
  echo "  429 = rate limited, wait 5 minutes"
  echo "  400 = malformed request"
fi
