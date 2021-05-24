"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
import zzim.views as zzim
import user.views as user


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user', zzim.listItem),
    path('user/<str:id>', zzim.viewOtherUserItem),
    path('item/<uuid:id>', zzim.viewItem),
    path('item/<uuid:id>/edit', zzim.editItem),
    path('item/<uuid:id>/purchased', zzim.setPurchasedItem),
    path('item/<uuid:id>/delete', zzim.deleteItem),
    path('item/add', zzim.addItem),
    path('user/signup', user.join),
    path('user/signin', user.login),
    path('user/signout', user.logout),
]
