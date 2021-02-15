from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse("Hello World")
def contact(request):
    return HttpResponse("I am Contact Page")