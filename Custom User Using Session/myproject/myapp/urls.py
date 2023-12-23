from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('signout/',views.signout,name='signout'),
    path('change_password/',views.change_password,name='change_password'),
    path('company_home/',views.company_home,name='company_home'),
    path('applicant_home/',views.applicant_home,name='applicant_home'),
    
    

]