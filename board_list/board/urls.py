from django.urls import path, re_path, include
from board.views import *

urlpatterns = [
    path('board-list/', BoardList.as_view(),),
    # re_path(r'board-list/board-page/(?P<product_id>[\d]+)$', BoardPage.as_view(), name='product_id'),
    path('board-list/board-page/<slug:board_slug>/', BoardPage.as_view()),
    path('categories/<path:name>/', CategoriesView.as_view(),)
]