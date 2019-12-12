
from django.http import HttpResponse
from django.template import loader

def hello(request):
    return HttpResponse("hello")

def Page1(request):
    #Get index.html
    template = loader.get_template('appone/entreprise.html')

    context = {
        'pictures': [
            {
                'filename': 'img1.jpg'
            },
            {
                'filename': 'img2.jpg'
            },
        ]

    }



    return HttpResponse(template.render(context , request))#All Values acces in my context

