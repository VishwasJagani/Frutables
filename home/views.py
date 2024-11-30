from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from home.models import *
from django.db.models import *

# Create your views here.

def base(request):
    std = ''
    if 'userid' in request.session:
        userid = request.session['userid']
        std = register.objects.get(id=userid) 

    a = Contact.objects.get()
    return std,a

def home(request):
    user = base(request)

    slide = slider.objects.all()
    a = product.objects.all()
    b = category.objects.all()  

    context = {
        "row":user[0], 
        "contact":user[1], 
        "slider":slide, 
        "a":a, 
        "b":b,
    }

    return render(request, "home/index.html" , context)

def shop(request):
    user = base(request)

    a = product.objects.all()
    b = category.objects.all()
    c = subcategory.objects.all()

    ran = len(a)

    d = product.objects.all().order_by('?')[:ran-2]

    if 'search' in request.POST:
        search = request.POST['text']
        a = product.objects.filter(name__icontains = search)
    
    context = {
        "row":user[0], 
        "contact":user[1], 
        "a":a, 
        "b":b, 
        "c":c, 
        "d":d,
    }

    return render(request, "home/shop.html", context)

def product_detail(request):
    user = base(request)

    context = {
        "row":user[0], 
        "contact":user[1],
    }

    return render(request , "home/product_detail.html", context)

def contact(request):
    user = base(request)

    a = Contact.objects.get()

    context = {
        "row":user[0] , 
        "a":a, 
        "contact":user[1],
    }

    return render(request , "home/contact.html", context)

def testimonial(request):
    user = base(request)

    context = {
        "row":user[0] , 
        "contact":user[1],
    }

    return render(request, "home/testimonial.html", context)

def register_page(request):

    if 'register' in request.POST:
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        number = request.POST['number']
        gender = request.POST['gender']
        password = request.POST['password']
        confirm = request.POST['confirm']
        address = request.POST['address']
        city = request.POST['city']
        country = request.POST['country']
        pincode = request.POST['pincode']
        image = request.FILES['image']

        if not register.objects.filter(email=email):
            if confirm == password:
                b = make_password(password)
                obj = register(
                    fname = fname,
                    lname = lname,
                    email = email,
                    number = number,
                    gender = gender,
                    password = b,
                    address = address,
                    city = city,
                    country = country,
                    pincode = pincode,
                    image = image,
                )
                obj.save()
                request.session['userid'] = obj.id
                return redirect(reverse("home"))

            else:
                messages.error(request, "Please Check Your Confirm Password")
                return redirect(reverse("register_page"))
        else:
            messages.error(request,"This Email is already register with us")
            return redirect("register_page")

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
