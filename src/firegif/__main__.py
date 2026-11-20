
import logging
import os
import uuid
from pathlib import Path

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

BASE_DIR = Path(__file__).resolve().parents[2]
INPUT_DIR = BASE_DIR / "input"
MAX_FILE_SIZE = 15 * 1024 * 1024

INPUT_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    await update.message.reply_text(
        "سلام! به FireGIF خوش اومدی. 🔥\n"
        "فعلاً یک عکس بفرست تا دریافتش رو آزمایش کنیم."
    )


async def receive_photo(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    message = update.message

    if not message or not message.photo:
        return

    photo = message.photo[-1]

    if photo.file_size and photo.file_size > MAX_FILE_SIZE:
        await message.reply_text("حجم عکس بیشتر از ۱۵ مگابایت است.")
        return

    filename = f"{uuid.uuid4().hex}.jpg"
    destination = INPUT_DIR / filename

    try:
        telegram_file = await photo.get_file()
        await telegram_file.download_to_drive(
            custom_path=str(destination)
        )

        await message.reply_text(
            "عکس با موفقیت دریافت شد! 🔥\n"
            "در مرحله بعد افکت‌ها را اضافه می‌کنیم."
        )

        logger.info("Photo saved: %s", filename)

    except Exception:
        logger.exception("Photo download failed")
        await message.reply_text(
            "دریافت عکس ناموفق بود. دوباره تلاش کن."
        )


def main() -> None:
    token = os.environ.get("TELEGRAM_BOT_TOKEN")

    if not token:
        raise RuntimeError("TELEGRAM_BOT_TOKEN is not set.")

    application = (
        Application.builder()
        .token(token)
        .build()
    )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(
        MessageHandler(filters.PHOTO, receive_photo)
    )

    logger.info("FireGIF bot is starting...")
    application.run_polling()


if __name__ == "__main__":
    main()
    
