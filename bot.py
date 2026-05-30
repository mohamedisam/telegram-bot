import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8003734279:AAFacok5TpWIo4r7cfu14rOp2Pxp-9vvrx0"

FILES_DIR = "files"

async def list_files(update: Update, context: ContextTypes.DEFAULT_TYPE):
    files = os.listdir(FILES_DIR)

    if not files:
        await update.message.reply_text("لا توجد ملفات.")
        return

    msg = "📂 الملفات:\n"
    for f in files:
        msg += f"- {f}\n"

    msg += "\nأرسل اسم الملف لتحميله."

    await update.message.reply_text(msg)


async def send_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file_name = update.message.text.strip()
    path = os.path.join(FILES_DIR, file_name)

    if os.path.exists(path):
        with open(path, "rb") as f:
            await update.message.reply_document(f)
    else:
        await update.message.reply_text("الملف غير موجود ❌")


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", list_files))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_file))

    print("البوت يعمل ✅")
    app.run_polling()


if __name__ == "__main__":
    main()