from django.db import models
# Create your models here.

from django.contrib.auth import get_user_model
class PNR(models.Model):
    User=get_user_model()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    pnr=models.IntegerField(default=0)
    train_number=models.IntegerField(default=0)
    source_station=models.CharField(max_length=100,default='')
    destination_station=models.CharField(max_length=100 , default='')
    distance=models.IntegerField(default=0)
    
    def __str__(self):
        return 'pnr details'

    def user_info(self):
        return f"User: {self.user.username}"
    
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    founded = models.DateField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name="books")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    published_date = models.DateField()
    genres = models.ManyToManyField("Genre", related_name="books")
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    join_date = models.DateField(auto_now_add=True)
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    order_date = models.DateTimeField(auto_now_add=True)
    shipped = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="order_items")
    quantity = models.PositiveIntegerField()
    price_at_purchase = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} × {self.book.title}"

