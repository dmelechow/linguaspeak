from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='auth-login'),
    path('signup/', views.signup, name='auth-signup')
]
