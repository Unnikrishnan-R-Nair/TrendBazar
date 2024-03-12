from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import post_save

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

    size_object = models.ManyToManyField(Size, null=True)

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

    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')

    created_date = models.DateTimeField(auto_now_add=True)

    updated_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    
    def __str__(self):

        return self.owner.username
    

    @property
    def basket_total(self):

        cart_items = self.cartitems.filter(is_order_placed=False)

        total = 0

        if cart_items:

            for item in cart_items:

                total += item.item_total

        return total
    

    @property
    def get_cart_items(self):

        qs = self.cartitems.filter(is_order_placed=False)

        return qs




class BasketItem(models.Model):

    basket_object = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='cartitems')

    product_object = models.ForeignKey(Product, on_delete=models.CASCADE)

    size_object = models.ForeignKey(Size, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)

    created_date = models.DateTimeField(auto_now_add=True)

    updated_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    is_order_placed = models.BooleanField(default=False)


    @property
    def item_total(self):

        return self.product_object.price * self.quantity
    

    

class Order(models.Model):

    user_object = models.ForeignKey(User, on_delete=models.CASCADE, related_name='myorders')

    basket_item_objects = models.ManyToManyField(BasketItem)

    delivery_address = models.CharField(max_length=250)

    phone = models.CharField(max_length=12)

    email = models.CharField(max_length=100)

    pay_options = (
        ('online', 'online'),
        ('cod', 'cod')
    )

    payment_mode = models.CharField(max_length=100, choices=pay_options, default='cod')

    order_id = models.CharField(max_length=200, null=True)

    is_paid = models.BooleanField(default=False)

    order_status = (
        ('order_confirmed', 'Order confirmed'),
        ('dispatched', 'Dispatched'),
        ('in_transit', 'In transit'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),

    )

    status = models.CharField(max_length=200, choices=order_status, default='order_confirmed')

    created_date = models.DateTimeField(auto_now_add=True)

    updated_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)





def create_basket(sender, instance, created, **kwargs):

    if created:

        Basket.objects.create(owner=instance)


post_save.connect(sender=User, receiver=create_basket)


    



