from django.urls import path
from . import views

app_name = 'personal_area'

urlpatterns = [
    path('', views.panel, name='panel'),
    path('/<int:id>', views.link_id, name='one_link')
]
