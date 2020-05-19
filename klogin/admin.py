from django.contrib import admin
from .models import Registration
# Register your models here.

@admin.register(Registration)      #Here I am registering my models so as to get tables in admin page
class AdminUser(admin.ModelAdmin):
#    list_display = ("username","fname","lname","phone","email","")
    search_fields = ("username","fname","phone","email")

