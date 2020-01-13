from django.shortcuts import render
from .utils import postview

def index(request):
    result = postview()



    return render(request, 'post/index.html', {'post':'고양이', 'post_list':result})
# Create your views here.
