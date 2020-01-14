from django.urls import path, include
from . import views
from . import utils

app_name='post'
urlpatterns = [
    path('result/', views.index, name='index'),
    path('', views.homepage, name='home'),
]