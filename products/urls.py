from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name='home'),
    path('products/',views.our_prouducts,name='products'),
    path('order/<int:order_id>/',views.order_buy,name='order'),
    path('privacy-policy/',views.privacy,name='privacy'),
    path('refund-policy/',views.refund,name='refund'),
    path('contact-us/',views.contact_us,name='contact_us'),
]
