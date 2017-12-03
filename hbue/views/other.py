from django.http import HttpResponse

def about(request):
    return HttpResponse("About Us")

def rule(request):
    return HttpResponse("Use Rule")

def blog(request):
    return HttpResponse("Our Blog")
