from django.shortcuts import render



def index(request):
    data = {
        'title': 'Главная страница',
        'values':['Some','Hello', '123' ]
    }

    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html' )


def contact(request):
    return render(request, 'main/contact.html' )

def shipment(request):
    return render(request, 'main/shipment.html' )

def payment(request):
    return render(request, 'main/payment.html' )