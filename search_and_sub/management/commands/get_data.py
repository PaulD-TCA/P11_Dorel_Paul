#! /usr/bin/env python3
# coding: utf-8

from django.core.management.base import BaseCommand, CommandError
from search_and_sub.models import Product
import json
import requests

from search_and_sub.management.commands import constants

class Command(BaseCommand):
    """
    Script who generate the data base "p8_pur_beurre_db".
      1. Get data from OpenFoodFacts.
      2. Data base filling :Table "Product".
    """
    def handle(self, *args, **options):
        toto1 = constants.CATEGORIES
        for categorie in constants.CATEGORIES:
            categories_id = constants.CATEGORIES.index(categorie)+1
            for nutrition_grade in constants.NUTRITION_GRADES:
                resp = requests.get(constants.URL_PART_1+categorie+
                    constants.URL_PART_2+nutrition_grade+constants.URL_PART_3)
                data = resp.json()
                nb_prods = int(data["count"])
                page_s = int(data["page_size"])
                row_w = 0
                p_id = 1
                if page_s <= nb_prods:
                    maxproduct = page_s
                else:
                    maxproduct = nb_prods
                while row_w < maxproduct:
                    try:

                        p_id = p_id + 1
                        p_code = data["products"][row_w]["code"]
                        p_name = data["products"][row_w]["product_name"]
                        p_name = p_name.replace('"', "'")
                        p_nut_gr = data["products"][row_w]["nutrition_grade_fr"]
                        p_ca_tags = data["products"][row_w]["categories_tags"]
                        p_ca_tags = str.join(",",p_ca_tags)
                        p_url = constants.URL_OPEN_FOOD_FACTS + p_code
                        p_image_url = data["products"][row_w]["image_url"]
                        p_fat = data["products"][row_w]["nutriments"]["fat"]
                        p_salt = data["products"][row_w]["nutriments"]["salt_100g"]
                        p_sugars = data["products"][row_w]["nutriments"]["sugars_value"]
                        p_saturated_fat = data["products"][row_w]["nutriments"]["saturated-fat"]
                        row_w = row_w + 1
                        print(p_name)

                        prod_to_add = Product.objects.create(p_code=p_code,
                            p_name=p_name, p_nutrition_grade_fr=p_nut_gr,
                            p_categories_tags=p_ca_tags, p_url=p_url,
                            p_image_url=p_image_url, p_fat=p_fat, p_salt=p_salt,
                            p_sugars=p_sugars, p_saturated_fat=p_saturated_fat)
                        prod_to_add.save()
                    except:
                        row_w = row_w + 1
