from django.db import models
from random import randint
from django.contrib.auth.models import User
# Create your models here.

class Items(models.Model):
    category=models.CharField(max_length=100,default="others")
    name=models.CharField(max_length=100, default="abc")
    price=models.IntegerField()
    description=models.TextField(null=True)
    img=models.ImageField()
    cart=[]
    def remove(self,product):
        item=Items.object.filter(name=product)
        if item in self.cart:
            self.cart.remove(item)

    class Order(models.Model):
        product=models.ManyToManyField(Items)
        owner=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    #    order_id=randint(1,10000)
        is_ordered=models.BooleanField(default=False)
        ordered_date=models.DateField(auto_now=True)

    # def get_cart_items(self):
    #     return self.product.all()


    def get_cart_total(self):
        print(Order.objects.filter(is_ordered=False))
        total=sum([item.product for item in Order.objects.filter(is_ordered=False)])
        return total

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    cart_product=models.ManyToManyField(Items,blank=True)

'''
class Cart:
    cart=[]
    def add(self,product):
        if Items.object.get(name=product):
           self.cart.append(Items.object.filter(name=product))

    def remove(self,product):
        item=Items.object.filter(name=product)
        if item in self.cart:
            self.cart.remove(item)

'''


