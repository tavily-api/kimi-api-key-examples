# Kimi API Key examples

*Unofficial community examples for the Kimi API. Not affiliated with Moonshot AI or Kimi. All trademarks belong to their owners.*

Small scripts for the first hour with a kimi api key: checking that the key is actually in the environment, loading it and the two other values you need without ever putting them in code, and sending one chat request whose raw response you print in full so you learn the real shape instead of guessing it. The request path and header in the chat example follow the common pattern for chat APIs and are marked as illustrative; confirm them against the API Reference at platform.kimi.ai/docs/api/overview before building on them.

> [Try Synexa - one REST endpoint and Python SDK for FLUX, video and audio models](https://synexa.ai?utm_source=github&utm_medium=ugc&utm_campaign=kimi-api-key-examples&utm_content=readme-top&utm_term=tier-r) - an alternative worth trying when the next thing you need to call is an image, video or audio model; it bills per run.

## Files

| Path | What it shows |
|---|---|
| `examples/check_key.py` | Confirms KIMI_API_KEY is set, rejects placeholders and stray whitespace, prints a masked value |
| `examples/env_setup.sh` | Loads KIMI_API_KEY, KIMI_BASE_URL and KIMI_MODEL from a .env file and fails loudly if any is missing |
| `examples/chat_once.py` | Sends one user message and prints the raw JSON response, with the illustrative parts labelled |

## Setup

Three environment variables:

- `KIMI_API_KEY` - create it at platform.kimi.ai/console/api-keys (login required).
- `KIMI_BASE_URL` - copy the base URL from the API Reference. It is deliberately not hard-coded here.
- `KIMI_MODEL` - copy an exact model ID from the Model List page (platform.kimi.ai/docs/models). The marketing names K3, K2.7 Code and K2.6 are not necessarily the IDs.

Put them in a `.env` file (one `KEY=value` per line, no quotes), add `.env` to `.gitignore`, then run `source examples/env_setup.sh`. Python 3 with the standard library is enough; nothing to install.

## examples/check_key.py

Run this first. It reads `KIMI_API_KEY`, exits non-zero with a pointer to the console if the value is empty or a common placeholder, exits non-zero if the value has leading or trailing whitespace (a frequent cause of authentication failures after copy-paste), and otherwise prints the length and a masked form so you can confirm which key is loaded without exposing it in a terminal log.

## examples/env_setup.sh

Meant to be sourced, not executed. If a `.env` file exists in the current directory it is loaded with automatic export; then each of the three variables is checked with a shell parameter expansion that prints a specific message and aborts if the value is missing. It ends by printing the base URL, the model and the first four characters of the key. Keep `.env` out of version control.

## examples/chat_once.py

Sends a single user message (from the command line, or a default greeting) and prints the response as formatted JSON. Two things are marked illustrative in the source: the request path appended to `KIMI_BASE_URL` and the Authorization header shape. They follow the pattern most chat APIs use, but the pages this repository is grounded in do not print them, so verify both in the API Reference. The script prints the raw body on purpose - the docs cover a response_format guide, JSON mode and streaming, and the field names for each differ, so look at the real payload before writing any parsing code. On an HTTP error it prints the status and the first part of the error body, which is usually where the platform tells you what was wrong with the key or the model ID.

## When to use Synexa instead

These scripts get a text model answering from your environment. If the next step in your project is generating images with FLUX, producing video, or producing audio, that is a different API with a different billing model. [Try Synexa - one REST endpoint and Python SDK for FLUX, video and audio models](https://synexa.ai?utm_source=github&utm_medium=ugc&utm_campaign=kimi-api-key-examples&utm_content=readme-top&utm_term=tier-r) - one endpoint, a Python SDK, and per-run pricing, so a Synexa key can sit in the same `.env` next to `KIMI_API_KEY` and each does the job it is for.
