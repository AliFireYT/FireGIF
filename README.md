# FireGIF

A Telegram bot for applying playful effects and text to photos, GIFs, videos, and stickers.

## Project status

Early development. The first milestone is a working Telegram bot skeleton; media processing will be added behind a separate engine module.

## Architecture

- **Telegram layer:** Python and `python-telegram-bot`
- **Processing engine:** Pillow for still images; FFmpeg for animated/video media
- **Deployment:** intended to run on an always-on server, independent of the developer's phone
- **Source control:** GitHub

Cloudflare Workers can be evaluated for webhook/routing tasks, but they do not directly run this Python + FFmpeg application. The processing worker needs a compatible server/container runtime.

## Local development

1. Install Python 3.11+ and FFmpeg.
2. Install dependencies: `pip install -r requirements.txt`
3. Set the bot token as an environment variable named `TELEGRAM_BOT_TOKEN`.
4. Run: `python -m firegif`

Never commit bot tokens, API keys, or other secrets.

## Current features

- [x] Initial project structure
- [x] Basic Telegram `/start` handler
- [ ] Receive and download media
- [ ] Effect selection
- [ ] Text overlay (including Persian)
- [ ] MP4/GIF export
- [ ] Server deployment
