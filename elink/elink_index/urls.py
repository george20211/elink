from django.contrib.auth.views import LogoutView 
from django.urls import path
from . import views

app_name = 'elink_index'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:linkeds>', views.open_link, name='open_link'),
    path('<str:linkeds>/secure_link', views.open_secure_link, name='open_secure_link'),
] 