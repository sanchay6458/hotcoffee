from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import HeaderFooter,BoddySection1,BoddySection2,BoddySection3,BoddySection4
def coffee(request):
    header=HeaderFooter.objects.get(id=1)
    section1=BoddySection1.objects.all()
    section2=BoddySection2.objects.all()
    section3=BoddySection3.objects.all()
    section4=BoddySection4.objects.all()
    return render(request,'index.html',{'head':header,'sec1':section1,'sec2':section2,'sec3':section3,'sec4':section4})
def desc(request):
    # template_name = 'index.html' 
    return render(request,'page.html')


# Create your views here.
