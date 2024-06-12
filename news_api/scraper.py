import requests
from bs4 import BeautifulSoup
from django.utils import timezone
from news.models import News    

def scrape_forex_news():
    url = 'https://www.forexfactory.com/news'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    news_items = soup.find_all('div', class_='news-article')

    for item in news_items:
        title = item.find('h2').text.strip()
        content = item.find('p').text.strip()
        published_at = timezone.now()

        if not News.objects.filter(title=title).exists():
            News.objects.create(
                title=title,
                content=content,
                published_at=published_at
            )

if __name__ == '__main__':
    scrape_forex_news()