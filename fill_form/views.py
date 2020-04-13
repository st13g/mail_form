from django.shortcuts import render


# Create your views here.
def get_demo(request):
    return render(request,'fill_form/index.html')
