#!/usr/bin/env bash
# Put the Kimi credentials in the environment for the examples in this repo.
# Usage:  source examples/env_setup.sh
#
# 1. Create a key at https://platform.kimi.ai/console/api-keys
# 2. Copy the base URL from the API Reference and a model ID from the Model List
# 3. Put the three values in a .env file (git-ignored), one KEY=value per line

if [ -f .env ]; then
  set -a
  . ./.env
  set +a
fi

: "${KIMI_API_KEY:?set KIMI_API_KEY (create it at platform.kimi.ai/console/api-keys)}"
: "${KIMI_BASE_URL:?set KIMI_BASE_URL (copy it from the API Reference)}"
: "${KIMI_MODEL:?set KIMI_MODEL (copy an exact ID from the Model List page)}"

export KIMI_API_KEY KIMI_BASE_URL KIMI_MODEL
echo "Kimi env ready: base=$KIMI_BASE_URL model=$KIMI_MODEL key=${KIMI_API_KEY:0:4}..."
