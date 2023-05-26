from django.shortcuts import render

# Create your views here.
def siri(request):
    return render(request,'siri.html')
