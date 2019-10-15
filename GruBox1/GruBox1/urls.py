from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from Students import views
from django.contrib.auth import views as authview

urlpatterns = [
    path('home/',views.home),
    path('accounts/', include('django.contrib.auth.urls'),name='login'), 
    path('admin/', admin.site.urls),
    #path('',views.loginpage),
    path('',views.StudentDetails),
    path('Topper/',views.ClassTopper),
    path('subjectopper/',views.SubjectTopper),
]
