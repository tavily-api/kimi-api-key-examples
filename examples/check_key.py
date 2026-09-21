'''Check that KIMI_API_KEY is set and looks usable, without printing it.'''
import os
import sys

key = os.environ.get('KIMI_API_KEY', '')
placeholders = {'', 'your-key-here', 'changeme', 'xxx', 'todo'}

if key.strip().lower() in placeholders:
    sys.exit('KIMI_API_KEY is not set. Create one at platform.kimi.ai/console/api-keys and export it.')

if key != key.strip():
    sys.exit('KIMI_API_KEY has leading or trailing whitespace; re-export it without quotes or spaces.')

masked = key[:4] + '...' + key[-4:] if len(key) > 8 else '****'
print(f'KIMI_API_KEY is set ({len(key)} chars): {masked}')
print('Never commit this value. Keep it in the environment or a git-ignored .env file.')
