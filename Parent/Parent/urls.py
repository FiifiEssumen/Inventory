"""Parent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import include ,url
from django.contrib.auth import views as auth_views
from Child import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from Child.api import Storemanager
# from Child.api import Inventory
# from tastypie.api import api
# from Child.api.resources import Storemanagerresoucee,Inventoryresource
# Django error __init__() takes 1 positional argument but 2 were given had this error and had to rectify by adding "as_view()" to LoginView and LogoutVeiw




urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'',include('Child.urls')),
    url(r'^login/$',auth_views.LoginView.as_view(),name='login'),
    url(r'^logout/$',auth_views.LogoutView.as_view(),name='logout',kwargs={'next_page':'/'}),
    url(r'^signup/$',views.signup,name='signup'),
]

urlpatterns += staticfiles_urlpatterns()






