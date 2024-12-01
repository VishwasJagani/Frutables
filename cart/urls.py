
from django.urls import path , include
from .views import *

urlpatterns = [
 
    path('',cartview,name="cart"),
    path('cart1/<int:id>',cart1,name="cart1"),
    path('cartdelete/<int:id>',cartdelete,name="cartdelete"),

]