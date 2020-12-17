from django.contrib import admin
from Child.models import Storemanager
from Child.models import Inventory

# Register your models here.
admin.site.register(Storemanager)
admin.site.register(Inventory)