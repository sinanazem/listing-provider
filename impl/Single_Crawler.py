import json
SALE_URL = "https://es.wallapop.com/app/search?category_ids=200&filters_source=quick_filters&order_by=newest&longitude=-3.69196&latitude=40.41956&operation=buy"
RENT_URL = "https://api.wallapop.com/api/v3/real_estate/search?category_ids=200&filters_source=quick_filters&operation=rent&order_by=newest&longitude=-3.69196&latitude=40.41956"

class SingleCrawler:

    def __init__(self):
        pass

    def crawl_single(self, response, card) -> dict:
        """
       This function scrapes every necessary information from a single page.
       this information contains title, description, contact info, any feature
       and amenity, no. beds and baths, and others.
       a guide to what you need to get from the page is reading the MappingTemplate
       and the following dict.

       ATTENTION: every value in outputted dict has to be string (
       including lists and dicts and others)
       """

        title = card['content'].get('title')
        description = card['content'].get('storytelling')
        city = card['content']['location'].get('city')
        price = card['content'].get('price')
        currency = card['content'].get('currency')
        listing_type = card['content'].get('operation')
        number_of_bedrooms = card['content'].get('rooms')
        number_of_baths = card['content'].get('bathrooms')
        property_type = card['content'].get('type')
        small_images = [img['small'] for img in card['content']['images']]
        large_images = [img['large'] for img in card['content']['images']]
        number_of_parking = card['content'].get('garage')
        floor_area = card['content'].get('surface')

        latitude = response['search_point']['latitude']
        longitude = response['search_point']['longitude']

        crawled_attributes_json = {
            "url": None,
            "title": title,
            "description": description,
            "location": None,  # the main neighborhood
            "city": city,
            "price": price,
            "priceCurrency": currency,
            "propertyType": property_type,  # e.g. house, apartment, condo, etc.
            "landUseType": None,  # residential or commercial
            "listingType": listing_type,  # sale or rent
            "numberOfBedrooms": number_of_bedrooms,
            "numberOfBaths": number_of_baths,
            "numberOfParking": number_of_parking,
            "floorArea": floor_area,
            "latitude": latitude,
            "longitude": longitude,
            "amenities": None,
            "smallImages": small_images,
            "largeImages": large_images,
            "isAgent": None,
            "full_name": None,
            "realEstate": None,
            "contact_phone": None,
            "email": None
            # and any other information you find necessary
        }
        return crawled_attributes_json

