from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index, auth_view, verify_view, SignUp, home

app_name = 'accounts'

urlpatterns = [
    path('', index, name='index'),
    path('accounts/login/', auth_view, name='login'),
    path('accounts/verify/', verify_view, name='verify'),
    path('accounts/signup/', SignUp.as_view(), name='signup'),
    path('accounts/user/', home, name='home'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
