from django.shortcuts import render, HttpResponse

def homepage(request):
    return HttpResponse("Hello everybody")

def test(request):
    return render(request, "test.html")

def second(request):
    return HttpResponse("test 2 page")
