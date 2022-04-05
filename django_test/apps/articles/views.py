from django.http import HttpResponse

def index(request):
    return HttpResponse("Dzirun Danil Viktorovich")

def test(request):
    return HttpResponse("26.07.2001")

