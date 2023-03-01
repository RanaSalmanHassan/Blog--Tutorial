from django.urls import path
from . import views
app_name = 'loginapp'
urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login_user', views.login_page, name='login'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
]
