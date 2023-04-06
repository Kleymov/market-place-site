from django.shortcuts import render
from django.views.generic import ListView 
from django.http import JsonResponse
from .models import *

# Create your views here.
class BoardList(ListView):
    template_name = 'boards.html'
    context_object_name = 'items'

    def dispatch(self, request, *args, **kwargs):
        return super(BoardList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        items = Board.objects.all()
        return items
 
    
class BoardPage(ListView):
    template_name = 'board_page.jinja'
    context_object_name = 'product_data'

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.item = 2
        if 'board_slug' in self.kwargs:
            product_slug = self.kwargs['board_slug']
            self.item = Board.objects.get(slug=product_slug)
        return super(BoardPage, self).dispatch(request, *args, **kwargs)

    def get_object(self):
        return self.item
    
    def get_queryset(self):
        return {'item':self.item, 'request': self.request}
    

class CategoriesView(ListView):
    template_name='category.html'
    context_object_name = 'products'

    def dispatch(self, request, *args, **kwargs):
        self.category = Category.objects.get(slug=kwargs['name'])
        return super(CategoriesView, self).dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        self.products = Board.objects.filter(categories__name=self.category)
        return self.products
    
    def get_object(self):
        return self.products


