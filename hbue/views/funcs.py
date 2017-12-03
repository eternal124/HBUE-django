from django.shortcuts import render
from django.http import Http404

def modalBox():
    # input： username, password, remember
    return HttpResponse("Sign In modelBox")