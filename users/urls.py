from django.urls import path
from .views import *

app_name = "users"
urlpatterns = [
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
]