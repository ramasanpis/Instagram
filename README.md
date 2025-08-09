# IG AI Bot (Telegram-controlled)

This project provides a Python-based Instagram automation bot that:
- Generates images via an image API (Pollinations by default).
- Generates captions via an OpenRouter/OpenAI-compatible endpoint.
- Queues posts in a local SQLite DB.
- Provides a Telegram bot interface to generate, preview, approve, and post images.
- Uploads to Instagram using `instagrapi` (or swap for Graph API).

IMPORTANT: **Do NOT put real secrets into public places.** Fill the `.env` file locally (see `.env.example`).

## Quick start
1. Create a virtualenv and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. Copy `.env.example` to `.env` and fill your keys.
3. Run:
   ```bash
   python main.py
   ```

## Files
- `main.py` - starts the Telegram bot and initializes DB.
- `config.py` - loads environment variables.
- `generator.py` - image + caption generation.
- `instagram_client.py` - wrapper around `instagrapi`.
- `telegram_bot.py` - Telegram handlers and control logic.
- `queue_db.py` - simple SQLite queue.
- `logger_config.py` - logging setup.
- `.env.example` - example environment variables (placeholders).

## Security
- Use environment variables or a secret manager for credentials.
- Do not paste keys into chat or public repositories.
