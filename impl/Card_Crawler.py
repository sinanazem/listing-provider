from typing import Tuple, List, Any

from bs4 import BeautifulSoup
import json

SALE_URL = "https://es.wallapop.com/app/search?category_ids=200&filters_source=quick_filters&order_by=newest&longitude=-3.69196&latitude=40.41956&operation=buy"
RENT_URL = 'https://api.wallapop.com/api/v3/real_estate/search?category_ids=200&filters_source=quick_filters&operation=rent&order_by=newest&longitude=-3.69196&latitude=40.41956'


class CardCrawler:

    def __init__(self):
        pass

    def __get_cards_from_html_doc(self, response) -> List[dict]:
        """
       this function only finds elements (if scraping or api call) of each card
       """
        cards = response['search_objects']

        return cards

    def __get_urls_and_ids(self, cards: list) -> Tuple[List[str], List[Any]]:
        """
       using cards outputted from scrape_cards_from_html_doc, this function
       finds urls and ids of each listing.
       ATTENTION: some listing urls are created using listing_ids and the direct
       url is not mentioned in the listing data. Using listing id, it is possible
       to make urls. → domain/listing_id
       """
        urls = []
        url_ids = []

        # your code here

        return urls, url_ids

    def crawl_source(self, response) -> List[dict]:
        cards = self.__get_cards_from_html_doc(response)
        return cards


if __name__ == "__main__":
    import requests
    response = requests.get(RENT_URL).json()
    obj = CardCrawler()\

    print(obj.crawl_source(response=response))
