from django.urls import path, include
from .views import *
from board.views import BoardList

urlpatterns = [
    path('', BoardList.as_view(),),
    path('cart/', CartView.as_view()),
    path('add-to-cart/', AddToCart.as_view()),
    path('delete-from-cart/', DeleteFromCart.as_view()),
    path('change-quantity/', ChangeQuantity.as_view()),
]