from django.shortcuts import render
from . models import college
from . models import teacher


# Create your views here.
def home(request):
    object=college.objects.all()
    teach=teacher.objects.all()
    return render(request,"index.html",{'obj':object,'teach':teach})

def about(request):
    return render(request,"about.html")