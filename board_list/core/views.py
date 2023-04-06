from django.shortcuts import render
from django.views.generic import ListView 
from django.http import JsonResponse
from user.models import User
from board.models import Board
import json


def main(request):
    return render(request, 'main.jinja/', {})



class CartView(ListView):
    template_name = 'cart/cart.jinja'
    context_object_name = 'products'

    def dispatch(self, request, *args, **kwargs):
        self.products_in_cart = {}
        try:
            cart = json.loads(request.user.cart)
    
            for key, value in cart.items():
                self.products_in_cart[Board.objects.get(id=key)] = value

        except:
            pass

        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        print(self.products_in_cart)
        return self.products_in_cart # TODO: Переименовать
    
    
class AddToCart(ListView):
    def post(self, request, *args, **kwargs):
        # Условие проверяет авторизован ли пользователь 
        if request.user.id is not None:
            user = User.objects.get(id=request.user.id) 

            # Получение корзины пользователя
            try:
                user_cart = json.loads(user.cart)
            except:
                user_cart = {}

            
            # Ниже: обработка запроса, если пользователь добавляет товар в корзину
            product = json.loads(request.body) # Получаем словарь с данными о товаре, который нужно поместить в корзину

            """
            Из запросы получаем корзину пользователя.
            Если корзина пуста, то помещаем в нее строку json с информацией о товаре.
            Если корзина не пуста, то добавляем данные о товаре уже в существующую корзину.
            """
            for key, value in product.items():
                # Добавляем товар в корзину пользователя
                try:
                    user_cart[key] += value
                except:
                    user_cart[key] = value # Если товара нет, то создадим его в корзине

            # Сохранение обновленной корзины
            user.cart = json.dumps(user_cart)
            user.save()
        
        return JsonResponse({'erorr': 'пользователь не авторизован'}) # HACK: Не знаю что возвращать, если пользователь не авторизован 
    

class DeleteFromCart(ListView):
    def post(self, request, *args, **kwargs):
        # Условие проверяет авторизован ли пользователь 
        if request.user.id is not None:
            # Ниже: обработка запроса, если пользователь удаляет товар из корзину
            user = User.objects.get(id=request.user.id) 
            user_cart = json.loads(user.cart)
        
            product = json.loads(request.body) # Данные о товаре, который нужно удалить

            for key, value in product.items():
                del user_cart[key]

            # Сохранение обновленной корзины
            user.cart = json.dumps(user_cart)
            user.save()
            
        return JsonResponse({'erorr': 'пользователь не авторизован'})

class ChangeQuantity(ListView):
    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id) 
        user_cart = json.loads(user.cart)

        product = json.loads(request.body) # Данные о товаре, количество которого нужно поменять

        for key, value in product.items():
            user_cart[key] = value

        # Сохранение обновленной корзины
            user.cart = json.dumps(user_cart)
            user.save()
            
        return JsonResponse({'erorr': 'пользователь не авторизован'})