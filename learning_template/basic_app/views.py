from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'templates/index.html')


def other(request):
    return render(request,'templates/other.html')

def relative(request):
    return render(request,'templates/relative_template.html')
