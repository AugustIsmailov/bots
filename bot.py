import os
import telebot

# Ваш персональный ID для отправки сообщений вам
YOUR_TELEGRAM_ID = '6345377425'

# Получение токена бота из переменной окружения
TOKEN = '7408629249:AAF8sVuXwHd6b9gOT7wfyrLB84LD-dIIy94'  # Убедитесь, что у вас есть эта переменная окружения

# Создание экземпляра бота
bot = telebot.TeleBot(TOKEN)

# Функция для старта бота
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я Анонимный Бот Чата Tokyo_mlbb. Хотите оставить анонимное сообщение? Тогда скорее пишите его!🤍")

# Функция для получения анонимного сообщения и пересылки его вам
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_message = message.text
    bot.send_message(chat_id=YOUR_TELEGRAM_ID, text=f"Анонимное сообщение: {user_message}")
    bot.reply_to(message, "Ваше сообщение было отправлено анонимно!")

# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)
