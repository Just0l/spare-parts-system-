from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginPage, name='index'),
    path('logout/', views.LogoutPage, name='index'),
    path('home/', views.HomePageView.as_view(), name='index'),
    path('Workshop/', views.Workshop, name='index'),
    path('Workshop/Addservice/', views.Addservice, name='index'),
    path('Workshop/Delete/', views.Delete, name='index'),
    path('Workshop/Update/', views.Update, name='index'),
    path('Workshop/Appointment/', views.ShowAppointment, name='index'),
]