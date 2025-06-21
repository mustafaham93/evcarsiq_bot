
from telegram import Update, InputMediaPhoto
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os

TOKEN = os.getenv("TOKEN")
CHANNEL_USERNAME = "@evcarsiraq"

async def handle_car_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    if not msg.photo or not msg.caption:
        await msg.reply_text("📸 أرسل صور السيارة مع كتابة التفاصيل بالوصف.")
        return
    media = [InputMediaPhoto(media=ph.file_id) for ph in msg.photo]
    await context.bot.send_media_group(chat_id=CHANNEL_USERNAME, media=media)
    await context.bot.send_message(chat_id=CHANNEL_USERNAME, text=msg.caption)
    await msg.reply_text("✅ تم استلام بيانات سيارتك وتم نشرها في القناة.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.PHOTO & filters.Caption(), handle_car_post))
    app.run_polling()
