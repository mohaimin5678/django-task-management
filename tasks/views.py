from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    # work with db
    # transform data
    # data pass
    # Http respose / Json response
    return HttpResponse("Welcome to the task management system")

def contact(request):
    return HttpResponse("<h1 style='color:red'>This is contact page</h1>")


def show_task(request):
    return HttpResponse("This is the task page")

def show_specific_task(request, id):
    return HttpResponse(f"This is a special task page {id}")