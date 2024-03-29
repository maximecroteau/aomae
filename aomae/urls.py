from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop', views.shop, name='shop'),
    path('contact', views.contact, name='contact'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('thankyou', views.thankyou, name='thankyou'),
    path('shop_<slug:filt>', views.shop_filter, name='shop'),
    path('product_<int:pk>', views.product, name='product'),
    path('about', views.about, name='about')
]