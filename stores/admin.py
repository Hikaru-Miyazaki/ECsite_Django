from django.contrib import admin
from .models import (
    Products, ProductPictures, ProductTypes,
    Manufacturers
)
# Register your models here.

admin.site.register(
    [Products, ProductPictures, ProductTypes, Manufacturers]
)