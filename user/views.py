import os
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.urls import reverse
from home.models import *

# Create your views here.

def user_profile(request):
    std = ''

    if 'userid' in request.session:
        userid = request.session['userid']
        std = register.objects.filter(id=userid).get()

    return render(request, "user/user_profile.html",{"row":std})

def profile_edit(request):
    
    if 'userid' in request.session:
        userid = request.session['userid']
        std = register.objects.filter(id=userid).get()

        if 'profile_edit' in request.POST:
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            number = request.POST['number']
            address = request.POST['address']
            country = request.POST['country']
            city = request.POST['city']
            pincode = request.POST['pincode']

            if len(request.FILES) != 0:
                if len(std.image) > 0:
                    os.remove(std.image.path)
                    std.image = request.FILES['image']
                std.fname = fname
                std.lname = lname
                std.email = email
                std.number = number
                std.address = address
                std.country = country
                std.city = city
                std.pincode = pincode

                std.save()
                return redirect("user_profile")

    return render(request, "user/user_profile_edit.html",{"row":std})

def change_pass(request):

    if 'userid' in request.session:
        userid = request.session['userid']
        std = register.objects.filter(id=userid).get()

        if 'change_pass' in request.POST:
            old = request.POST['oldpassword']
            new = request.POST['newpassword']
            confirm = request.POST['confirm']
            
            b = make_password(new)

            if check_password(old,std.password):
                if new == confirm:
                    std.password = b
                    std.save()
                    return redirect("home")
                
                else:
                    messages.error(request, "Please Check Your Confirm Password")
                    return redirect(reverse("change_pass"))
                
            else:
                messages.error(request, "Please Check Your Old Password")
                return redirect(reverse("change_pass"))

    return render(request, "user/change_pass.html",{"row":std})