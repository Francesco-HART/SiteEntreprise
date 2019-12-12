from django.http import HttpResponse
from django.template import loader

def firtview(request):
    return HttpResponse("Salut")
