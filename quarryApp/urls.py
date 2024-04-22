"""E_Quarry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('index/',views.index),
    path('contractor_reg/', views.contractor_reg),
    path('login/', views.login),
    path('about/', views.about),
    path('contact/', views.contact),

    #master
    path('category/', views.category),
    path('up_category/<int:ct_id>',views.up_category),
    path('update_category/',views.update_category),
    path('del_category/<int:ct_id>', views.del_category),

    path('product_type/', views.product_type),
    path('up_type/<int:tp_id>',views.up_type),
    path('update_type/',views.update_type),
    path('del_type/<int:tp_id>', views.del_type),

    path('type_spec/', views.type_spec),
    path('up_spec/<int:ts_id>',views.up_spec),
    path('update_spec/',views.update_spec),
    path('del_spec/<int:ts_id>', views.del_spec),

    path('emp_register/', views.emp_register),
    path('del_emp/<int:log_id>', views.del_emp),
    path('view_contractor/', views.view_contractor),
    path('approve_contractor/<int:log_id>', views.approve_contractor),
    path('del_contractor/<int:log_id>', views.del_contractor),
    path('order_view/', views.order_view),
    path('buy_view/', views.buy_view),
    path('pass_view/', views.pass_view),
    path('reply/', views.reply),
    path('ad_profile/', views.ad_profile),

    #Employee
    path('add_stock/', views.add_stock),
    path('up_stock/<int:tp_id>',views.up_stock),
    path('update_stock/', views.update_stock),
    path('order_details/', views.order_details),
    path('buy_details/', views.buy_details),
    path('deliver/<int:or_id>',views.deliver),
    path('view_pass_request/', views.view_pass_request),
    path('approve_pass/<int:ps_id>',views.approve_pass),
    path('reject_pass/<int:ps_id>',views.reject_pass),
    path('emp_profile/', views.emp_profile),
    path('reset_emp/', views.reset_emp),

    #Contractor
    path('contractor_reg/', views.contractor_reg),
    path('contractor_home/', views.contractor_home),
    path('add_vehicle/', views.add_vehicle),
    path('up_vehicle/<int:v_id>',views.up_vehicle),
    path('update_vehicle/',views.update_vehicle),
    path('del_vehicle/<int:v_id>', views.del_vehicle),

    path('pass_request/',views.pass_request),
    path('view_pass/',views.view_pass),

    path('order/<int:tp_id>', views.order),  
    path('order_product/', views.order_product), 
    path('order_now/', views.order_now),
    path('view_order/', views.view_order),

    path('buy/<int:tp_id>', views.buy),
    path('buy_product/', views.buy_product),
    path('buy_now/', views.buy_now),
    path('view_buy/', views.view_buy),
    
    path('contractor_profile/', views.contractor_profile),
    path('contractor_feedback/', views.contractor_feedback),

    path('reset_con/', views.reset_con),
    
    

    path('sign_out/', views.sign_out),

    path('master_reg/', views.master_reg),

]

