from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = "8986912431:AAGQkoabjMYi4fscovQ_qgSwxAHLhd86qZ8"
ADMIN_ID = 7494981584

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome!\n\nআপনার সমস্যাটি লিখে পাঠান। আমাদের টিম খুব দ্রুত উত্তর দেবে।"
    )

async def user_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    text = (
        f"📩 নতুন মেসেজ এসেছে\n\n"
        f"👤 {user.full_name}\n"
        f"🆔 {user.id}\n"
        f"@{user.username}\n\n"
        f"💬 {update.message.text}"
    )

    await context.bot.send_message(chat_id=ADMIN_ID, text=text)
    await update.message.reply_text("✅ আপনার মেসেজ গ্রহণ করা হয়েছে।")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, user_message))

app.run_polling()
