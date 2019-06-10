from django.http import HttpResponse

def welcome(request):
    print(request)
    return HttpResponse("I'm here to raise you!")

