from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def Homepage(request):
#     return HttpResponse("First django Assignment !")
     
def Homepage(request):
    return render(request,'FIRSTAPPLICATION\Homepage.html')


def Indexpage(request):
    return render(request,'FIRSTAPPLICATION\Indexpage.html')
 