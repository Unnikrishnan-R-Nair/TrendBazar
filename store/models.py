from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=200, unique=True)

    created_date = models.DateTimeField(auto_now_add=True)

    updated_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    
    def __str__(self):

        return self.name


class Size(models.Model):

    name = models.CharField(max_length=100, unique=True)

    created_date = models.DateTimeField(auto_now_add=True)

    updated_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    
    def __str__(self):

        return self.name
    



class Brand(models.Model):

    name = models.CharField(max_length=100, unique=True)

    created_date = models.DateTimeField(auto_now_add=True)

    updated_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    
    def __str__(self):

        return self.name
    

class Product(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField(null=True, blank=True)

    size_object = models.ManyToManyField(Size, on_delete=models.CASCADE)

    category_object = models.ForeignKey(Category, on_delete=models.CASCADE)

    brand_object = models.ForeignKey(Brand, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='product_images', null=True, blank=True, default='product_images/default.jpg')

    price = models.PositiveIntegerField()

    created_date = models.DateTimeField(auto_now_add=True)

    updated_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    
    def __str__(self):

        return self.title
    


class Basket(models.Model):

    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True)

    updated_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    
    def __str__(self):

        return self.owner.username
    


class BasketItem(models.Model):

    basket_object = models.ForeignKey(Basket, on_delete=models.CASCADE)

    product_object = models.ForeignKey(Product, on_delete=models.CASCADE)

    size_object = models.ForeignKey(Size, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)

    created_date = models.DateTimeField(auto_now_add=True)

    updated_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)






    



