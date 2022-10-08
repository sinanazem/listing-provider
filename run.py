import requests
from bs4 import BeautifulSoup
from impl.Card_Crawler import CardCrawler
from impl.Single_Crawler import SingleCrawler
from impl.Mapping import Mapping
from tester.unit_test import UnitTest
import json
SALE_URL = "https://es.wallapop.com/app/search?category_ids=200&filters_source=quick_filters&order_by=newest&longitude=-3.69196&latitude=40.41956&operation=buy"
RENT_URL = "https://api.wallapop.com/api/v3/real_estate/search?category_ids=200&filters_source=quick_filters&operation=rent&order_by=newest&longitude=-3.69196&latitude=40.41956"


class Runner:

    def __init__(self):
        self.cards = []
        self.card_ids = []
        self.singles = []
        self.mapped_listings = []
        self.card_crawler = CardCrawler()
        self.single_crawler = SingleCrawler()
        self.mapping = Mapping()

    def get_cards(self, url: str):
        headers = {}
        # response = requests.request('GET', url, headers=headers)
        response = requests.get(url).json()
        self.cards = self.card_crawler.crawl_source(response)

    def get_singles(self, url):
        headers = {}
        for card in self.cards:
            # response = requests.request('GET', url, headers=headers)
            response = requests.get(url).json()
            self.singles.append(self.single_crawler.crawl_single(response, card))

    # def map(self):
    #     for single in self.singles:
    #         self.mapped_listings.append(self.mapping.mapping_crawled_attributes(single))

    def run(self):
        for url in [RENT_URL]:
            self.get_cards(url)
            self.get_singles(url)
            # self.map()
        # return self.mapped_listings
        return self.singles


if __name__ == "__main__":
    mapped_listings = Runner().run()
    # UnitTest().test(mapped_listings)
    print(mapped_listings[0])


