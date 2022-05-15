
from unicodedata import name
from django.urls import path
from .views import HomeView, DetailView, AddPost, UpdatePost, DelPost, AddCategory, CategoryView, CategoryListView, LikeView ,AddComent

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('articls/<int:pk>', DetailView.as_view(), name='detail-articl'),
    path('add_post', AddPost.as_view(), name='add-post'),
    path('add_category/', AddCategory.as_view(), name='add-category'),
    path('articls/edit/<int:pk>', UpdatePost.as_view(), name='update-post'),
    path('articls/delet/<int:pk>', DelPost.as_view(), name='del-post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category_list/', CategoryListView, name='category-list'),
    path('likes/<int:pk>', LikeView, name='like-post'),
    path('articls/<int:pk>/coment/' , AddComent.as_view(),name='add-coment')
]
