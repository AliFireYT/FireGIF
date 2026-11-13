import logging
import os

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        await update.message.reply_text(
            "سلام! به FireGIF خوش اومدی. 🔥\n"
            "فعلاً نسخه آزمایشی رباته؛ دریافت و پردازش رسانه به‌زودی فعال می‌شه."
        )


def main() -> None:
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        raise RuntimeError(
            "TELEGRAM_BOT_TOKEN is not set. Set it as an environment variable."
        )

    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))

    logger.info("FireGIF bot is starting...")
    application.run_polling()


if __name__ == "__main__":
    main()
