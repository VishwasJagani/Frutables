from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import *

# Create your views here.

def base(request):
    std = ''
    if 'userid' in request.session:
        userid = request.session['userid']
        std = register.objects.get(id=userid) 
    # print(a)
    return std

def home(request):
    user = base(request)
    return render(request, "home/index.html" , {"row":user})

def shop(request):
    return render(request, "home/shop.html")

def product_detail(request):
    return render(request , "home/product_detail.html")

def contact(request):
    user = base(request)
    return render(request , "home/contact.html", {"row":user})

def testimonial(request):
    return render(request, "home/testimonial.html")

def register_page(request):

    if 'register' in request.POST:
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        gender = request.POST['gender']
        password = request.POST['password']
        confirm = request.POST['confirm']

        if confirm == password:
            b = make_password(password)
            obj = register(
                fname = fname,
                lname = lname,
                email = email,
                gender = gender,
                password = b,
            )
            obj.save()
            request.session['userid'] = obj.id
            return redirect(reverse("home"))

        else:
            messages.error(request, "Please Check Your Confirm Password")
            return redirect(reverse("register_page"))

    return render(request, "home/register.html")

def login_page(request):

    if 'login' in request.POST:
        email = request.POST['email']
        password = request.POST['password']

        if register.objects.filter(email=email):
            std = register.objects.get(email=email)
            if check_password(password,std.password):
                request.session['userid'] = std.id
                return redirect(reverse("home"))
            else:
                messages.error(request,"Please Check Your Password")
                return redirect("login_page")
        
        else:
            messages.error(request,"This Email is not register with us")
            return redirect("login_page")

    return render(request, "home/login.html")

def logout_page(request):
    del request.session['userid']
    return redirect("home")    