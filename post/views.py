import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import time

from .utils import postview

def index(request):
    post_company = request.GET['post_company']
    post_number = request.GET['post_number']
    data = postview(post_company, post_number)


    return render(request, 'post/index.html', {'post_all_detail': data})
# Create your views here.

@csrf_exempt
def homepage(request):



    if (request.method == 'POST'):

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        content = body["action"]
        post_company = content["params"]["post_company"]
        post_number = content["params"]["post_number"]
        data = postview(post_company, post_number)
        print(post_number)
        print(post_company)
        print(data)

        time.sleep(1)

        return JsonResponse(
            {
                "version": "2.0",
                "data": {
                    "post_company": post_company,
                    "post_number": post_number,
                    "post_detail": data,
                }
            }
        )

    return render(request, 'post/home.html')
