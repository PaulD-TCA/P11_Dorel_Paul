#! /usr/bin/env python3
# coding: utf-8

CATEGORIES = ["Boissons", "Viandes", "Produits laitiers", "Plats préparés",
                "Produits à tartiner", "Biscuits et gâteaux", "Charcuteries",
                "Epicerie", "Petit-déjeuners", "Fromages", "Desserts", "Sauces",
                "Produits de la mer", "Conserves", "Surgelés"]
NUTRITION_GRADES = ["A","B","C","D","E"]
URL_PART_1 = "https://fr.openfoodfacts.org/cgi/search.pl?action="\
            "process&tagtype_0=categories&tag_contains_0=contains&tag_0="
URL_PART_2 = "&tagtype_1=nutrition_grades&tag_contains_1=contains&tag_1="
URL_PART_3 = "&page_size=100&json=true"
#20 or 50 or 100 or 250 or 500 or 1000


URL_OPEN_FOOD_FACTS = "https://fr.openfoodfacts.org/produit/"
