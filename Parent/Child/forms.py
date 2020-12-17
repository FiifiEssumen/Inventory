from django import forms
from Child.models import Storemanager,Inventory
from django.forms import ModelForm

class StoreManagerForm(forms.ModelForm):
    class Meta:
        model = Storemanager
        fields = ('username', 'password','email')
        widgets = {
            'password': forms.PasswordInput(),

        }
class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ('productName','vendor','MRP','batchNum','quantity','status')