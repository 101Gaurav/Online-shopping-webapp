from django.contrib import admin
from .models import Items,Order
# Register your models here.
@admin.register(Items,Order)
class AdminUser(admin.ModelAdmin):
    search_fields = ("name","id")