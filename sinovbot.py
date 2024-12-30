from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Salomlashish funksiyasi
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('bot render serveri orqali yoqildi')

async def main():
    # Botni ishga tushurish
    token = '7981554834:AAE1yMVath0oAJSs-AWba5MR04rFu28Fg2M'  # Tokenni shu yerga joylang
    application = Application.builder().token(token).build()

    # CommandHandler orqali /start komandasini qo'shish
    application.add_handler(CommandHandler("start", start))

    # Botni ishga tushurish va polling qilish
    await application.run_polling()

# Agar sizning tizimingizda "event loop" muammosi bo‘lsa
# asyncio.run() ni bevosita ishlatib bo'lmaydi, lekin buni async metodda ishga tushirishingiz mumkin.
if __name__ == '__main__':
    import nest_asyncio
    nest_asyncio.apply()  # Bu usul orqali mavjud voqealar tsiklini yangilab olish mumkin.
    import asyncio
    asyncio.run(main())
