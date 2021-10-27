from django.shortcuts import render
import requests
from django.http import JsonResponse

def show(request):
    value = request.GET['Interest']
    # print(value)
    data={'ticker':value}
    row=requests.post("https://docker.api.srifintech.com/testassignment",data=data).json()
    # print(row)
    return JsonResponse(row,safe=False)

def IndexInterface(request):
    return render(request,'index.html')

