import os
import telebot

# Ваш персональный ID для отправки сообщений вам
YOUR_TELEGRAM_ID = '6345377425'

# Получение токена бота из переменной окружения
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')  # Токен подгружается из переменной окружения

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
    user_name = message.from_user.first_name  # Имя пользователя
    user_username = message.from_user.username  # Username пользователя (если есть)
    user_id = message.from_user.id  # ID пользователя

    # Формируем сообщение с информацией о пользователе
    if user_username:
        sender_info = f"{user_name} (@{user_username})"
    else:
        sender_info = f"{user_name} (ID: {user_id})"

    bot.send_message(chat_id=YOUR_TELEGRAM_ID, text=f"Анонимное сообщение от {sender_info}: {user_message}")
    bot.reply_to(message, "Ваше сообщение было отправлено анонимно!")

# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)