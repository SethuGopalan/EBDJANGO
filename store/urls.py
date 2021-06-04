from django.urls import path
# from django.urls import path

"""
import modules from store
"""
from  . import views

"""
allow acces to thr views
"""
app_name = 'store'

urlpatterns = [

        path("", views.all_products, name= "all_products"),

        # path('', views.product_all, name='product_all'),

]