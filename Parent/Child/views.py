from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DetailView
from Child.models import Storemanager, Inventory
from Child.forms import InventoryForm, StoreManagerForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# LoginMIxin is used to redirect unathorised users to another page


class AboutView(TemplateView):
    template_name = 'about.html'

class InventoryListView(ListView):
    template_name = 'Child/list.html'
    context_object_name = 'product_list'
    model = Inventory

    def get_queryset(self):
        return Inventory.objects.all()


class InventoryListDetail(DetailView):
    model = Inventory
# model was equal to InventoryForm


class UpdateInventoryView(LoginRequiredMixin,CreateView):
    login_url = '/login'
    redirect_field_name = 'Child/Inventory_detail.html'

    model = Inventory
    form_class = InventoryForm


class InventoryDeleteView(LoginRequiredMixin,DetailView):
    model = Inventory
    success_url = reverse_lazy('list') 



@login_required
def add_Inventory(request):
    # inventory = get_list_or_404(Inventory,pk=productId)
    if request.method == 'POST':
        form = InventoryFrom(request.POST)
        if form.is_valid():
            cdin = form.save()
            return redirect('list')
            # return redirect was equal to redirect_url

    else:
        form = InventoryForm()
    return render(request,'Child/inventory_form.html',{'form':form})


def remove_inventory(request,productId):
    inventory = Inventory(request)
    product = get_list_or_404(inventory,pk=productId)
    inventory.remove(product)
    return redirect('list')



# this function used to be user_login and i changed to login 
def login(self,request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect('detail') 
                return redirect(redirect_url)

            else:
                return HttpResponse("Account is not active")

        else:
                print("Someone tried to login")
                print("username: {} and password: {}".format(username,password)) 
                return HttpResponse("invalid user details") 

        
    else:
                return render(request,'Child/login.html',{})



def signup(request):
       if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           raw_password = form.cleaned_data.get('password1') 
           email = form.cleaned_data.get('email')
           user = authenticate(username=username, password=raw_password,email=email) 
        #  user = authenticate(request,username=username, password=raw_password,email=email) removed the request after comparing code

           login(request,user)
           return redirect('about')        

        else:
            form = UserCreationForm()
        return render(request,'signup.html',{'form': form})

 







# @login_required
# def logout(request):
#     return render(request, 'logout.html',{})




# class CreateInventoryView(LoginRequiredMixin,CreateView):
#     login_url = '/login/'
#     redirect_field_name = 'mysite/product_detail.html'
#
#     model = Inventory
#     form_class = InventoryForm


# @login_required
# def delete_Inventory(request, productId):
#    inventory = get_object_or_404(Inventory, pk=productId)
#    if request.method=='POST':
#         inventory.delete()
#
#         return redirect('url')
#    return render(request, 'inventory/delete_computer.html', {'computer': comp})

# @login_required
# def detail(request, productId):
#     inventory = get_object_or_404(Inventory, pk=productId)
#     return render(request, 'mysite/detail.html', {'form': form})



# changed the user_login function to login because of the reverse for login not found 
                # return render(request,'login/about.html',{})






# def my_login(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         username = form['username'].value()
#         password = form['password'].value()
#         user = authenticate(username=username,password=password)
#         if user:
#             login(request,user)
#             redirect_url = request.GET.get('next','Slife:home')
#             return redirect(redirect_url)
#         else:
#              messages.error(request,'Invalid Username or Password')
#     else:
#         form = LoginForm()
#         return render(request,'Slife/login.html',{'form':form})    

# def my_logout(request):
#     logout(request)
#     messages.success(request,'Logged out successfully')
#     return redirect('Slife:login')          