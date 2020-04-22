"""myweb URL Configuration

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
from django.urls import path
from POS import views

urlpatterns = [
    path('', views.my_login, name='login'),
    path('admin/', admin.site.urls),
    path('index/', views.home, name='index'),
    path('management/', views.management, name='management'),
    path('product_add/', views.product_add, name='Product_add'),
    path('product_edit/<int:product_id>', views.product_edit, name='Product_edit'),
    path('product_delete/<int:product_id>', views.product_delete, name='product_delete'),
    path('type_manage/', views.type_manage, name='type_manage'),
    path('type_delete/<int:type_id>', views.type_delete, name='type_delete'),
    path('type_edit/<int:type_id>', views.type_edit, name='type_edit'),
    path('add_type/', views.type_add, name='add_type'),
    path('add_to_cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('report/', views.report, name='report'),
    path('show_error/', views.show_error_404, name='error'),
    path('logout', views.my_logout, name='logout'),

]