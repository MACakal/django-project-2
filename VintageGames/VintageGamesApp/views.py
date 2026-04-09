from django.shortcuts import render

# Create your views here.
def indexTest(request):
    return render(request,"templates\index.html")
