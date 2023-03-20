from django.shortcuts import redirect, render

import omise

# models
from .models import *

# Create your views here.

omise_pkey = 'pkey_test_5v5o8fdsfm8vqe1xxx7'
omise_skey = 'skey_test_5v5o8hwz1y52vu829nx'

def home(request):
    return render(request, 'app_general/home.html')

def booking(request):
    if request.method == 'POST':
        getquantity = request.POST['quantity']
        getemail = request.POST['email']
        getimage = request.FILES.get('image')

        print(getquantity, getemail, getimage)

        booking = BookingModel(quantity=getquantity, email=getemail, image=getimage)
        booking.save()

        return redirect('checkout')

    return render(request, 'app_general/booking.html')

def checkout(request):
    price = 12345
    context = {
        'omise_pkey':omise_pkey,
        'price':price,
    }
    return render(request, 'app_general/checkout.html', context)

def creditpay(request):
    if request.method == 'POST':
        omiseToken = request.POST['omiseToken1']
        price = request.POST['price1']

        omise.api_secret = omise_skey

        charge = omise.Charge.create(
            amount=int(price),
            currency="thb",
            card=omiseToken,
            return_uri=request.build_absolute_uri('/success'),
        )
        print(charge.status)
        if charge.status == 'successful':
            return redirect('success')
        
    return render(request, 'app_general/creditpay.html')

def success(request):
    return render(request, 'app_general/success.html')