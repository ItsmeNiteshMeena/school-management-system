"""
URL configuration for lmproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('registration/',views.registration,name='registration'),
    path('admindash/',views.admindash,name='admindash'),
    path('option/',views.option,name='option'),
    path('stulogin/',views.stulogin,name='stulogin'),
    path('scheduled/',views.scheduled,name='scheduled'),
     path('queryform/<int:pk>',views.queryform,name='queryform'),   # name matches the queryform at the dashboard page 
    path('querydata',views.querydata,name='querydata'),
    path('allquery/<int:pk>',views.allquery,name='allquery'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('updatedate/<int:pk>',views.updatedata,name='updatedata'),
    path('search/<int:pk>',views.search,name='search')

]
