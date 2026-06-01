from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# # Вставь свой токен сюда
# import os
# TOKEN = os.environ.get("TOKEN")

# # Обработчик команды /start
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user = update.effective_user
#     await update.message.reply_text(
#         f"Привет, {user.first_name}! 👋\n"
#         f"Я твой бот. Рад познакомиться!"
#     )
    

# # Запуск бота
# def main():
#     app = ApplicationBuilder().token(TOKEN).build()
#     app.add_handler(CommandHandler("start", start))
#     print("Бот запущен...")
#     app.run_polling()

# if __name__ == "__main__":
#     main()



import telebot

# Вставь свой токен сюда
import os
TOKEN = os.environ.get("TOKEN")

bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой первый бот на Python.")

# Обработчик любых текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Запуск бота
bot.infinity_polling()
