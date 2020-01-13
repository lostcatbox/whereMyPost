from django.urls import path, include
from . import views
from . import utils

urlpatterns = [
    path('', views.index, name='index'),
    path('crawling/', utils.postview(), name='crawling'),
]