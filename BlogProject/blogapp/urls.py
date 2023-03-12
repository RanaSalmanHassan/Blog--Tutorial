from django.urls import path
from . import views
app_name = 'blogapp'
urlpatterns = [
    path('create_blog',views.Create_Blog,name='create_blog'),
    path('edit_blog/<pk>',views.Edit_Blog.as_view(),name='edit_blog'), 
    path('delete_blog/<pk>',views.Delete_Blog.as_view(),name='delete_blog'), 
]