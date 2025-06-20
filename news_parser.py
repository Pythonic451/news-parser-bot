import requests
from bs4 import BeautifulSoup


def parse_habr_news(keywords):
    url = "https://habr.com/ru/flows/develop/articles/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = []
    for article in soup.find_all("article"):
        title = article.find("h2").text.strip()
        link = article.find("a")["href"]

        if any(word.lower() in title.lower() for word in keywords):
            articles.append({"title": title, "link": link})

    return articles


if __name__ == "__main__":
    keywords = ["Python", "ИИ", "GPT"]
    news = parse_habr_news(keywords)
    for item in news:
        print(f"{item['title']}\n{item['link']}\n")
