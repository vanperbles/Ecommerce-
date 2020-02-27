from django.urls import path
from . import views
from .views import ( HomeView,ItemDetailView,CheckoutView, add_to_cart,remove_from_cart,PaymentView,
                    AddCouponView, RequestRefundView, OrderSammaryView,popup,permit_user,search_api,
                     remove_single_item_from_cart)
app_name = 'shop'

urlpatterns = [

    path('', HomeView.as_view(),name="home-page"),
    path('product/<slug>',ItemDetailView.as_view(), name="product"),
    path('popup/', popup, name="popup"),
    path('ordersview', OrderSammaryView.as_view(), name="ordersview"),
    path('checkout', CheckoutView.as_view(), name="checkout"),
    path('add-to-cart/<slug>', add_to_cart, name="add-to-cart"),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,name='remove-single-item-from-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('create-item/', views.create_item, name='create-item'),
    path('permit-user/', views.permit_user, name='permit-user'),
    path('search/', views.search_api, name='search'),

]