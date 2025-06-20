from news_parser import parse_habr_news
from telegram_bot import send_to_telegram

def main():
    keywords = ["Python", "ИИ", "GPT"]
    news = parse_habr_news(keywords)

    TOKEN = "ВАШ_TELEGRAM_BOT_TOKEN"
    CHAT_ID = "ВАШ_CHAT_ID"
    
    for item in news:
        message = f"{item['title']} \n https://habr.com{item['link']}"
        send_to_telegram(TOKEN, CHAT_ID, message)

if __name__ == "__main__":
    main()
