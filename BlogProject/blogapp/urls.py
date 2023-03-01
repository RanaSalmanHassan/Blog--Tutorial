from django.urls import path
from . import views
app_name = 'blogapp'
urlpatterns = [
    path('create_blog',views.Create_Blog,name='create_blog')
]