'''Send one chat message to the Kimi API using values from the environment.

ILLUSTRATIVE PARTS: the request path appended to KIMI_BASE_URL and the
Authorization header shape follow the common chat-API pattern. The pages this
repo is grounded in do not print them; confirm both in the API Reference at
platform.kimi.ai/docs/api/overview before relying on this script.
'''
import json
import os
import sys
import urllib.error
import urllib.request

api_key = os.environ.get('KIMI_API_KEY')
base_url = os.environ.get('KIMI_BASE_URL')  # copy from the API Reference
model = os.environ.get('KIMI_MODEL')        # copy an exact ID from the Model List

missing = [name for name, value in (
    ('KIMI_API_KEY', api_key),
    ('KIMI_BASE_URL', base_url),
    ('KIMI_MODEL', model),
) if not value]
if missing:
    sys.exit('set ' + ', '.join(missing) + ' first (see examples/env_setup.sh)')

prompt = ' '.join(sys.argv[1:]) or 'Say hello in one sentence.'

# ILLUSTRATIVE: verify the path in the API Reference.
url = base_url.rstrip('/') + '/chat/completions'
payload = {
    'model': model,
    'messages': [{'role': 'user', 'content': prompt}],
}
req = urllib.request.Request(
    url,
    data=json.dumps(payload).encode('utf-8'),
    headers={
        # ILLUSTRATIVE: verify the header shape in the API Reference.
        'Authorization': 'Bearer ' + api_key,
        'Content-Type': 'application/json',
    },
    method='POST',
)

try:
    with urllib.request.urlopen(req, timeout=60) as resp:
        body = json.load(resp)
except urllib.error.HTTPError as err:
    detail = err.read().decode('utf-8', 'replace')[:500]
    sys.exit(f'HTTP {err.code} from {url}: {detail}')
except urllib.error.URLError as err:
    sys.exit(f'could not reach {url}: {err.reason}')

# Print the raw shape first. Field names differ between plain chat, JSON mode
# and streaming (see the response_format guide), so look before you parse.
print(json.dumps(body, indent=2, ensure_ascii=False)[:4000])
