import telebot

def send_to_telegram(token, chat_id, message):
    bot = telebot.TeleBot(token=token)

    bot.send_message(chat_id=chat_id, text=message)

if __name__ == "__main__":
    # Получите токен у @BotFather и ID чата
    TOKEN = "ВАШ_TELEGRAM_BOT_TOKEN"
    CHAT_ID = "ВАШ_CHAT_ID"
    
    test_message = "Привет, это тест из Python!"
    send_to_telegram(TOKEN, CHAT_ID, test_message)
