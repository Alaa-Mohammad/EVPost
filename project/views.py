from django.shortcuts import HttpResponse

def home(request):
    print(request.META.get('HTTP_REFERER'))
    return HttpResponse('HHHHHH')

