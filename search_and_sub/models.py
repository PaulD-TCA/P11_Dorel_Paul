from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    """fields of Product table"""
    p_code = models.CharField(max_length=50)
    p_name = models.CharField(max_length=200)
    p_nutrition_grade_fr = models.CharField(max_length=1)
    p_categories_tags = models.CharField(max_length=1000)
    p_url = models.URLField()
    p_image_url = models.URLField()
    p_fat = models.FloatField(null=True)
    p_salt = models.FloatField(null=True)
    p_sugars = models.FloatField(null=True)
    p_saturated_fat = models.FloatField(null=True)

    def __str__(self):
        return self.p_name


class Backup(models.Model):
    """fields of Backup table"""
    b_date = models.DateTimeField(auto_now_add=True)
    p_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.b_date
