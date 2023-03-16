#from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views
def HELLO_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello!, its my project')
def now_date_view(request):
    if request.method == 'GET':
        return HttpResponse('16.03.2023')
def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse('Goodbye, user')