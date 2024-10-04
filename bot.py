import os
import telebot

# Ваш персональный ID для отправки сообщений вам
YOUR_TELEGRAM_ID = '6345377425'

# Получение токена бота
TOKEN = '7408629249:AAF8sVuXwHd6b9gOT7wfyrLB84LD-dIIy94'

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
    user_name = message.from_user.username if message.from_user.username else message.from_user.first_name
    user_id = message.from_user.id
    
    # Отправляем сообщение с информацией о пользователе
    bot.send_message(
        chat_id=YOUR_TELEGRAM_ID, 
        text=f"Анонимное сообщение от @{user_name} (ID: {user_id}): {user_message}"
    )
    
    # Подтверждение отправки пользователю
    bot.reply_to(message, "Ваше сообщение было отправлено анонимно!")

# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)