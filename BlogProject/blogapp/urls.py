from django.urls import path
from . import views
app_name = 'blogapp'
urlpatterns = [
    path('create_blog',views.Create_Blog,name='create_blog'),
    path('',views.blog_home,name='blog_home'),
    path('edit_blog/<pk>',views.Edit_Blog.as_view(),name='edit_blog'), 
    path('delete_blog/<pk>',views.Delete_Blog.as_view(),name='delete_blog'), 
    path('blog_details/<pk>',views.Blog_Details,name='blog_details'), 
    path('like_blog/<pk>',views.like_blog,name='like_blog'), 
    path('search_blogs',views.search_blogs,name='search_blogs'), 
]