# # myapp/api.py
# from tastypie.resources import ModelResource
# from Child.models import Storemanager
# from Child.models import Inventory

# class StoremanagerResource(ModelResource):
#     class Meta:
#         queryset = Storemanager.objects.all()
#         resource_name = 'Storemanager'
# Storemanager_resource = StoremanagerResource()


# class InventoryResource(ModelResource):
#     class Meta:
#         queryset = Inventory.objects.all()
#         resource_name = 'Inventory'
# Inventory_Resource = InventoryResource()               


# The class has no member error was corrected becasue of the linting i posted at the setting.json file.