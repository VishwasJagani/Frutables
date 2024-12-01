
from django.urls import path
from .views import *

urlpatterns = [
    path("" , home, name="home"),
    path("shop/" , shop, name="shop"),
    path("contact/" , contact, name="contact"),
    path("testimonial/" , testimonial, name="testimonial"),
    path("register/" , register_page, name="register_page"),
    path("login/" , login_page, name="login_page"),
    path("logout_page/" , logout_page, name="logout_page"),
    path("product_detail/<int:id>" , product_detail, name="product_detail"),
    path("Fruits/" , fruits, name="Fruits"),
    path("Vegetables/" , vegetables, name="Vegetables"),
]