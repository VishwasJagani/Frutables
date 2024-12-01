from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from home.models import *
from .models import *
from home.views import base

# Create your views here.

def cartview(request):
    user = base(request)
    sum = 0
    rate = 30
    
    a = cart.objects.filter(user_id = user[0].id).all()

    if 'cartsubmit' in request.POST:
        qty = request.POST.getlist('qty[]')
        cart_ids = request.POST.getlist('cart_ids[]')        
        i = 0

        for x in cart_ids:
            obj = cart.objects.get(id=x)
            obj.qty = int(qty[i])
            obj.total = int(qty[i])* int(obj.product_id.price)
            obj.save()
            i+=1    
    
    elif not a:
        return HttpResponse("<h1>Your Cart Is Empty")
    
    for i in a:
        sum += i.total

    context = {
        "row":user[0], 
        "contact":user[1], 
        "a" : a,
        "sum" : sum,
        "rate" : rate,
    }

    return render(request, "cart/cart.html", context)

def cart1(request,id):

    a = product.objects.filter(id=id).get()

    if 'userid' in request.session:
        userid = request.session['userid']
        std = register.objects.get(id=userid)

        total = 1 * a.price

        obj = cart(
            user_id = std,
            product_id = a,
            qty = 1,
            total = total,
        )
        obj.save()
        return redirect(reverse("cart"))

    return render(request, "cart/cart.html")

def cartdelete(request,id):
    std = cart.objects.filter(id=id).get()
    std.delete()
    return redirect(reverse("cart"))
