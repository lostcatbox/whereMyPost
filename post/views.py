from django.shortcuts import render
from .utils import postview

def index(request):
    post_company = request.GET['post_company']
    post_number = request.GET['post_number']
    data = postview(post_company, post_number)


    return render(request, 'post/index.html', {'post':'고양이', 'post_list':data})
# Create your views here.

def homepage(request):

    return render(request, 'post/home.html')
