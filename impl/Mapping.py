import json
import yaml


class Mapping:

    def __init__(self):
        self.attribute_mapper = {}  # load json file
        self.mapping_template = {}  # DO NOT LOAD HERE

    def __convert_to_mapper_ids(self, type_or_feature, namelat_value):
        type_or_feature_json = self.attribute_mapper[type_or_feature]
        for index in range(len(type_or_feature_json)):
            type_or_feature_dict = type_or_feature_json[index]
            feat_dict = type_or_feature_dict["nameLat"]
            if feat_dict.lower() == namelat_value.strip().lower():
                attr_id = type_or_feature_dict["id"]
            try:
                attr_type_id = type_or_feature_dict["typeId"]
            except KeyError:
                attr_type_id = ""

        return attr_id, attr_type_id

    def mapping_crawled_attributes(self, crawled_json: dict) -> dict:
        """
        this function find some ids and type ids from attribute_mapper based on
        crawled attributed of single page, and information is added to the template
        file
        """
        self.mapping_template = {}  # load json file
        # your code here

        return self.mapping_template
