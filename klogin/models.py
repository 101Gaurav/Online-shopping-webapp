from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

'''
class Registration(models.Model):
    username = models.CharField(max_length=100,default="ABC")
    fname = models.CharField(max_length=100,default="ABC")
    lname=models.CharField(max_length=100,null=True)
#    dob = models.DateField(default="yyyy-mm-dd")
#    phone = models.CharField(max_length=10,default="1234")
    email = models.EmailField(default="abc@xyz.com")
    password = models.CharField(max_length=30,default="a12")
'''


class Registration(models.Model):
    one_2_one = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    dob = models.DateField(null=True)
    phone = models.CharField(max_length=10, default="1234")


'''  
    def verify_pass(self, password):
        return pbkdf2_sha256.verify(password, self.password)
'''
