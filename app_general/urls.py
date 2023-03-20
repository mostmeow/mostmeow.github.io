from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('booking', views.booking, name='booking'),
    path('checkout', views.checkout, name='checkout'),

    path('creditpay', views.creditpay, name='creditpay'),

    path('success', views.success, name='success'),
]