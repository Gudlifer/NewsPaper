from django.urls import path
from .views import *

urlpatterns = [
    path('', PostsList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', PostSearch.as_view(), name='post_search'),
    path('news/create/', NWCreate.as_view(), name='news_create'),
    path('news/<int:pk>/update/', NWUpdate.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', NWDelete.as_view(), name='news_delete'),
    path('articles/create/', ARCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/update/', ARUpdate.as_view(), name='articles_update'),
    path('articles/<int:pk>/delete/', ARDelete.as_view(), name='articles_delete'),
    path('subscriptions/', subscriptions, name='subscriptions'),

 ]