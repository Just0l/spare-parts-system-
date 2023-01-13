from django.shortcuts import render, redirect
from SCP.models import Services, Workshop_Image, Appointment
from User.models import User
import datetime
from django.contrib.auth.forms import AuthenticationForm


from django.contrib.auth import authenticate, login, logout

from django.views.generic import TemplateView
from .forms import AddserviceForm

# Create your views here.

# def index(request):
#     return render(request, 'SCP/index.html')



def LoginPage(request):
  user=User.objects.get(id=3)
  login(request, user)

  response = redirect('/Workshop/')
  return response
   



def LogoutPage(request):
  logout(request)
  response = redirect('/Workshop/')
  return response



    
      
    


class HomePageView(TemplateView):
    template_name = 'SCP/index.html'





#class Workshop(TemplateView):
#    template_name = 'SCP/Workshop.html'

def Workshop(request):
   if request.user.is_authenticated:
      if request.user.role == 'WORKSHOP':
         obj = Services.objects.all().filter(W_id=request.user.id)
         
         obj1 = Workshop_Image.objects.get(W_id=User.objects.get(id=request.user.id))
         
         context = {
            'obj': obj,
            'obj1': obj1,

         }

         return render(request, 'SCP/Workshop.html', context)
      else:
         response = redirect('/home/')
         return response
   else:
         response = redirect('/home/')
         return response





def ShowAppointment(request):
   if request.user.is_authenticated:
    if request.user.role == 'WORKSHOP':
     datenow= datetime.datetime.now().date()+datetime.timedelta(days=3)
     print (datenow)
     obj = Appointment.objects.all().filter(W_id=request.user.id,Date__range=[datetime.datetime.now().date(), datenow])
     CID=[]
     for n in obj:
      CID.append([User.objects.get(id=n.C_id.id),n,Services.objects.get(id=n.S_id.id)])
     context = {
        'obj': obj,
        'obj1': CID

     }

     return render(request, 'SCP/Appointment.html', context)
    else:
      response = redirect('/home/')
      return response

   else:
         response = redirect('/home/')
         return response









def Addservice(request):
   if request.user.is_authenticated:
      if request.user.role == 'WORKSHOP':
         Add_form = AddserviceForm()
         
         if request.method =="POST":
            Add_form = AddserviceForm(request.POST)
            if Add_form.is_valid():
                  Services.objects.create(
                     W_id =User.objects.get(id=request.user.id,role='WORKSHOP'),
                     name = Add_form.cleaned_data['name'],
                     price = Add_form.cleaned_data['price']
                  )
                  response = redirect('/Workshop/')
                  return response
         context = {
            "form":Add_form
         }

         return render(request, 'SCP/Addservice.html', context)
      else:
         response = redirect('/home/')
         return response
   else:
         response = redirect('/home/')
         return response









def Delete(request):
   if request.user.is_authenticated:
      if request.user.role == 'WORKSHOP':
         a = request.GET.get('DeleteID')
         if Services.objects.all().filter(id=a,W_id=request.user.id).exists():
            obj = Services.objects.get(id=a,W_id=request.user.id)
            
            obj.delete()
         response = redirect('/Workshop/')
         return response
      else:
         response = redirect('/home/')
         return response
   
   else:
         response = redirect('/home/')
         return response







def Update(request):
   if request.user.is_authenticated:
      if request.user.role == 'WORKSHOP':
         Add_form = AddserviceForm()
         
         if request.method =="POST":
            Add_form = AddserviceForm(request.POST)
            if Add_form.is_valid():
                  service = Services.objects.get(id=request.GET.get('UpdateID'),W_id=request.user.id)
                  service.name = Add_form.cleaned_data['name']
                  service.price = Add_form.cleaned_data['price']
                  service.save()
                  response = redirect('/Workshop/')
                  return response
         context = {
            "form":Add_form
         }
         return render(request, 'SCP/Updateservice.html', context)
      else:
         response = redirect('/home/')
         return response
   
   else:
         response = redirect('/home/')
         return response






