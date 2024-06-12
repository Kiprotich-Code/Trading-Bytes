import time
from django.core.management.base import BaseCommand
from news.scraper import scrape_forex_news

class Command(BaseCommand):
    help = 'Scrape Forex news and save to the database'

    def handle(self, *args, **kwargs):
        while True:
            scrape_forex_news()
            self.stdout.write(self.style.SUCCESS('Successfully scraped news.'))
            time.sleep(3600)