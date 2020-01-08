from django.shortcuts import render

def index(request):
    return render(request, 'post/index.html', {'post':'고양이'})
# Create your views here.
