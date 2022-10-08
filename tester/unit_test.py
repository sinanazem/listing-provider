
country_code = {
    "netherlands": 14,
    "france": 11,
    "spain": 13,
    "swiss": 17,
    "italy": 19,
    "india": 20,
    "denmark": 21,
    "sweden": 22
}

country = ""


class UnitTest:

    def __init__(self):
        self.cnt = country_code[country] - 1
        self.id = self.cnt * 100
        self.land_use_id = (self.cnt * 10 + 3) * 1000
        self.land_use_type_id = self.cnt * 1000 + 4
        self.property_id = (self.cnt * 10 + 2) * 1000
        self.property_type_id = self.cnt * 1000 + 3
        self.feature_id = (self.cnt * 10) * 1000
        self.feature_type_id = self.cnt * 1000 + 1
        self.tag_id = (self.cnt * 10 + 1) * 1000
        self.tag_type_id = self.cnt * 1000 + 2

    @staticmethod
    def __try_exists(dict_var, first, second, third):
        error = False
        if second is None:
            try:
                if first not in dict_var:
                    raise Exception
            except:
                print(f"could not find {first}.")
                error = True
        elif third is None:
            try:
                if second not in dict_var[first]:
                    raise Exception
            except:
                print(f"could not find {first}->{second}.")
                error = True
        else:
            try:
                if third not in dict_var[first][second]:
                    raise Exception
            except:
                print(f"could not find {first}->{second}->{third}")
                error = True
        return error

    def __check_not_null_and_type(self, mapped_listing):
        error = False
        error = error or self.__try_exists(mapped_listing, 'sourceId', None, None)
        error = error or self.__try_exists(mapped_listing, 'contactInfo', 'callNumber', None)
        error = error or self.__try_exists(mapped_listing, 'contactInfo', 'fullName', None)
        error = error or self.__try_exists(mapped_listing, 'contactInfo', 'type', None)
        error = error or self.__try_exists(mapped_listing, 'contactInfo', 'logoUrl', None)
        error = error or self.__try_exists(mapped_listing, 'contactInfo', 'nameLocal', None)
        error = error or self.__try_exists(mapped_listing, 'contactInfo', 'nameLat', None)
        error = error or self.__try_exists(mapped_listing, 'currentStatusId', None, None)
        error = error or self.__try_exists(mapped_listing, 'listingTypeId', None, None)
        error = error or self.__try_exists(mapped_listing, 'attributes', 'floorArea', 'unit')
        error = error or self.__try_exists(mapped_listing, 'values', 'currency', 'value')
        error = error or self.__try_exists(mapped_listing, 'sourceUrl', None, None)

        if not self.__try_exists(mapped_listing, 'location', None, None):
            if not self.__try_exists(mapped_listing, 'location', 'longitude', None) and type(mapped_listing['location']['longitude']) != float:
                print('longitude should be float not ', type(mapped_listing['location']['longitude']))
                error = True
            elif self.__try_exists(mapped_listing, 'location', 'longitude', None):
                error = True
            if not self.__try_exists(mapped_listing, 'location', 'latitude', None) and type(mapped_listing['location']['latitude']) != float:
                print('longitude should be float not ', type(mapped_listing['location']['latitude']))
                error = True
            elif self.__try_exists(mapped_listing, 'location', 'latitude', None):
                error = True

        if not self.__try_exists(mapped_listing, 'attributes', 'specifics', None):
            error = error or self.__check_id_ranges(mapped_listing)
        else:
            error = True

        if not self.__try_exists(mapped_listing, 'attributes', 'floorArea', 'value'):
            if not (type(mapped_listing['attributes']['floorArea']['value']) == int or mapped_listing['attributes']['floorArea']['value'] is None):
                print('floor area value is not in correct format (null or int)')
                error = True
            if type(mapped_listing['attributes']['floorArea']['value']) == int:
                if type(mapped_listing['attributes']['floorArea']['unit']) != str:
                    print('floor area unit should be sqm, sqft, ...')
                    error = True
        else:
            error = True

        if not self.__try_exists(mapped_listing, 'attributes', 'noBeds', None):
            if mapped_listing['attributes']['noBeds'] is not None and type(mapped_listing['attributes']['noBeds']) != int:
                print('number of beds should be of type int not ', mapped_listing['attributes']['noBeds'])
                error = True
        else:
            error = True
        if not self.__try_exists(mapped_listing, 'attributes', 'noBaths', None):
            if mapped_listing['attributes']['noBaths'] is not None and type(mapped_listing['attributes']['noBaths']) != int:
                print('number of beds should be of type int not ', mapped_listing['attributes']['noBaths'])
                error = True
        else:
            error = True
        if not self.__try_exists(mapped_listing, 'attributes', 'noParkings', None):
            if mapped_listing['attributes']['noParkings'] is not None and type(mapped_listing['attributes']['noParkings']) != int:
                print('number of beds should be of type int not ', mapped_listing['attributes']['noParkings'])
                error = True
        else:
            error = True

        if not self.__try_exists(mapped_listing, 'additionalInfo', None, None) and type(mapped_listing['additionalInfo']) != type([]):
            print('additional info should be array')
            error = True
        elif not self.__try_exists(mapped_listing, 'additionalInfo', None, None):
            for i, info in enumerate(mapped_listing['additionalInfo']):
                if 'key' not in info:
                    print(f'each additional info should have a key. while checking {i} additional info.')
                    error = True
                else:
                    if type(info['key']) != str:
                        print(f'key for additional info number {i} should be string.')
                        error = True
                if 'value' not in info:
                    print(f'each additional info should have a key. while checking {i} additional info.')
                    error = True
                else:
                    if type(info['value']) != str:
                        print(f'value for additional info number {i} should be string.')
                        error = True
        else:
            error = True

        if mapped_listing['listingTypeId'] == self.id + 1:
            error = error or self.__try_exists(mapped_listing, 'values', 'price', None)
            if not self.__try_exists(mapped_listing, 'values', 'price', None):
                if type(mapped_listing['values']['price']) != int and type(mapped_listing['values']['price']) != float:
                    print('price value should be int or float.')
                    error = True
        elif mapped_listing['listingTypeId'] == self.id + 2:
            error = error or self.__try_exists(mapped_listing, 'values', 'rent', None)
            error = error or self.__try_exists(mapped_listing, 'values', 'rentFrequency', None)
            if not self.__try_exists(mapped_listing, 'values', 'rent', None):
                if type(mapped_listing['values']['rent']) != int and type(mapped_listing['values']['rent']) != float:
                    print('rent value should be int or float.')
                    error = True

        if len(mapped_listing['media']) > 0:
            if 'isCover' in mapped_listing['media'][0]:
                if mapped_listing['media'][0]['isCover'] is not True:
                    print('cover photo is not defined.')
                    error = True
            for i, media in enumerate(mapped_listing['media']):
                error = error or self.__try_exists(media, 'type', None, None)
                error = error or self.__try_exists(media, 'photoSmallUrl', None, None)
                error = error or self.__try_exists(media, 'photoLargeUrl', None, None)
                error = error or self.__try_exists(media, 'isCover', None, None)
                if 'type' in media and media['type'] not in ['PHOTO', 'VIDEO']:
                    print(f'type for media number {i} should be PHOTO or VIDEO not ', media['type'])
                    error = True
                if 'photoSmallUrl' in media and (media['photoSmallUrl'] is None or media['photoSmallUrl'] == ""):
                    print(f'small photo url for media number  {i} should not be empty.')
                    error = True
                if 'photoLargeUrl' in media and (media['photoLargeUrl'] is None or media['photoLargeUrl'] == ""):
                    print(f'large photo url for media number  {i} should not be empty.')
                    error = True
                if 'isCover' in media and type(media['isCover']) is not bool:
                    print(f'is cover for media number {i} should be boolean.')
                    error = True

        return error

    def __check_id_ranges(self, mapped_listing):
        error = False
        if not (self.id < mapped_listing['sourceId'] < self.id + 4):
            print("source id is not within the right range: ", mapped_listing['sourceId'])
            error = True
        if mapped_listing['currentStatusId'] != self.id + 1:
            print('current status should be: ', self.id + 1)
            error = True
        if mapped_listing['listingTypeId'] not in [self.id + 1, self.id + 2]:
            print("listing type id is not within the right range: ", mapped_listing['listingTypeId'])
            error = True

        has_property_type = False
        has_landuse_type = False

        for i, specific in enumerate(mapped_listing['attributes']['specifics']):
            if specific['type'] not in ['LAND_USE_TYPE', 'PROPERTY_TYPE', 'PROPERTY_FEATURE', 'PROPERTY_TAG']:
                print(f"specifics' type in specific number {i} should be LAND_USE_TYPE, PROPERTY_TYPE, PROPERTY_FEATURE or PROPERTY_TAG not ", specific['type'])
                error = True
            if specific['typeId'] == self.land_use_type_id:
                has_landuse_type = True
                if not self.__try_exists(specific, 'id', None, None):
                    if specific['id'] == '':
                        error = True
                        print(f"land use id in specific {i} should not be empty")
                    elif not (self.land_use_id < specific['id'] < self.land_use_id + 3):
                        print(f"land use id in specific number {i} is not within the right range: ", specific["id"])
                        error = True
            elif specific['typeId'] == self.property_type_id:
                has_property_type = True
                if not self.__try_exists(specific, 'id', None, None):
                    if specific['id'] == '':
                        error = True
                        print(f"property type id in specific {i} should not be empty")
                    elif not (self.property_id < specific['id'] < self.property_id + 100):
                        print(f"property id in specific number {i} is not within the right range: ", specific["id"])
                        error = True
            elif specific['typeId'] == self.feature_type_id:
                if not self.__try_exists(specific, 'id', None, None):
                    if specific['id'] == '':
                        error = True
                        print(f"feature id in specific {i} should not be empty")
                    elif not (self.feature_id < specific['id'] < self.feature_id + 200):
                        print(f"feature id in specific number {i} is not within the right range: ", specific["id"])
                        error = True
            elif specific['typeId'] == self.tag_type_id:
                if not self.__try_exists(specific, 'id', None, None):
                    if specific['id'] == '':
                        error = True
                        print(f"tag id in specific {i} should not be empty")
                    elif not (self.tag_id < specific['id'] < self.tag_id + 100):
                        print(f"tag id in specific number {i} is not within the right range: ", specific["id"])
                        error = True
            else:
                print(f'type id for the specific number {i} is not within the right range.')
                error = True

        if not has_property_type:
            print('no property type was found in specifics.')
        if not has_landuse_type:
            print('no land use type was found in specifics.')

        return error

    def test(self, mapped_listings):
        for mapped_listing in mapped_listings:
            if mapped_listing is not None:
                print(mapped_listing)
                error = self.__check_not_null_and_type(mapped_listing)
                if not error:
                    print('this mapping is passed with no errors.')
        return

# if __name__ == '__main__':
#     UnitTest().test([])