import random
from search_and_sub.models import Product

class MenuBuild:
    """
    Built a random menu with products in database.
    """
    def random_starter(self):
        """
        Select a random entry in the database with a nutriscore A or B.
        """
        starters_list =[]
        list_of_starters = Product.objects.filter(
            p_categories_tags__icontains="starters",
            p_nutrition_grade_fr="a") | Product.objects.filter(
            p_categories_tags__icontains="starters",
            p_nutrition_grade_fr="b")
        for entry in list_of_starters:
            starters_list.append(entry.id)
        choosen_starter = random.choices(starters_list)
        essaisdeplus = Product.objects.filter(
            p_categories_tags__icontains="meals").exclude(
            p_categories_tags__icontains="beverages")
        return(choosen_starter)

    def random_main_dish(self):
        """
        Select a random main dish in the database with a nutriscore A or B.
        """
        main_dishes_list =[]
        list_of_main_dishes = Product.objects.filter(
            p_categories_tags__icontains="meals",
            p_nutrition_grade_fr="a").exclude(
            p_categories_tags__icontains="beverages" "starters") | Product.objects.filter(
            p_categories_tags__icontains="meals",
            p_nutrition_grade_fr="b").exclude(
            p_categories_tags__icontains="beverages" "starters")
        for main_dishes in list_of_main_dishes:
            main_dishes_list.append(main_dishes.id)
        choosen_main_dishes = random.choices(main_dishes_list)
        return(choosen_main_dishes)

    def random_dessert(self):
        """
        Select a random dessert in the database with a nutriscore A or B.
        """
        desserts_list =[]
        list_of_desserts = Product.objects.filter(
        p_categories_tags__icontains="desserts",
        p_nutrition_grade_fr="a") | Product.objects.filter(
        p_categories_tags__icontains="desserts",
        p_nutrition_grade_fr="b")
        for dessert in list_of_desserts:
            desserts_list.append(dessert.id)
        choosen_dessert = random.choices(desserts_list)
        return(choosen_dessert)
