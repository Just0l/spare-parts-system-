from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from SCP.models import Services, Workshop_Image, Appointment
from User.models import User
from itertools import chain


from django.views.generic import TemplateView
from .forms import AddserviceForm

# Create your views here.

# def index(request):
#     return render(request, 'SCP/index.html')

class LogIn(TemplateView):
    template_name = 'SCP/login.html'



class HomePageView(TemplateView):
    template_name = 'SCP/index.html'





#class Workshop(TemplateView):
#    template_name = 'SCP/Workshop.html'

def Workshop(request):
     obj = Services.objects.all().filter(W_id=3)
     
     obj1 = Workshop_Image.objects.get(W_id=User.objects.get(id=3))
     #print(obj1.image_field.url)
     
     context = {
        'obj': obj,
        'obj1': obj1,

     }

     return render(request, 'SCP/Workshop.html', context)





def ShowAppointment(request):
     obj = Appointment.objects.all().filter(W_id=3)
     obj1 = User.objects.all().filter(role='CUSTOMER')
     obj2 = Services.objects.all().filter(W_id=3)
     CID=[]
     for n in obj1:
        for i in obj2:
            for j in obj:
               if j.C_id == n:
                if j.S_id == i:
                  CID.append([n,j,i])
                
        
    
     
     
     
        
        
    
     
     context = {
        'obj': obj,
        'obj1': CID

     }

     return render(request, 'SCP/Appointment.html', context)









def Addservice(request):
     Add_form = AddserviceForm()
     
     if request.method =="POST":
        Add_form = AddserviceForm(request.POST)
        if Add_form.is_valid():
            #print(Add_form.cleaned_data['name'])
            Services.objects.create(
                W_id =User.objects.get(id=3,role='WORKSHOP'),
                name = Add_form.cleaned_data['name'],
                price = Add_form.cleaned_data['price']
            )
            response = redirect('/Workshop/')
            return response
     context = {
        "form":Add_form
     }

     return render(request, 'SCP/Addservice.html', context)









def Delete(request):
    a = request.GET.get('DeleteID')
    obj = Services.objects.get(id=a)
    
    obj.delete()
    response = redirect('/Workshop/')
    return response







def Update(request):
     Add_form = AddserviceForm()
     
     if request.method =="POST":
        Add_form = AddserviceForm(request.POST)
        if Add_form.is_valid():
            service = Services.objects.get(id=request.GET.get('UpdateID'))
            service.name = Add_form.cleaned_data['name']
            service.price = Add_form.cleaned_data['price']
            service.save()
            response = redirect('/Workshop/')
            return response
     context = {
        "form":Add_form
     }
     return render(request, 'SCP/Updateservice.html', context)





