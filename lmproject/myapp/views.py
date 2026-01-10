from django.shortcuts import render,redirect
from django.contrib import messages
from myapp.models import Student,Admin,Query
from django.db.models import Q


# Create your views here.
def home(request):
    return render(request,'home.html')

def option(request):
   return render(request,'option.html')



def stulogin(request):
      if request.method=='POST':
         email=request.POST.get('email')
         password=request.POST.get('password')
         # print(email,password)
         user=Student.objects.get(email=email)
         if user:
            data=Student.objects.get(email=email)  #extra line not need user me student ka object hai
            databasename=data.name
            databasepass=data.password
            if databasepass==password:
               return render(request,'studash.html',{'data':data})    #{{data}}
            else:
               x="password is not match"
               return render(request,'stulogin.html',{'msg':x})
         else:
            x="email does not register"
            return render(request,'registration.html',{'msg':x})
      else:
         return render(request,'stulogin.html')



def login(request):
      if request.method=='POST':
         email=request.POST.get('email')
         password=request.POST.get('password')
         # print(email,password)
         user=Admin.objects.get(email=email)
         if user:
            data=Admin.objects.get(email=email)  #extra line not need user me student ka object hai
            databasename=data.name
            databasepass=data.password
            if databasepass==password:
               return render(request,'admindash.html',{'data':data})    #{{data}}
            else:
               x="password is not match"
               return render(request,'login.html',{'msg':x})
         else:
            x="email does not register"
            return render(request,'registration.html',{'msg':x})
      else:
         return render(request,'login.html')
      
def scheduled(request):
   return render(request,'scheduled.html')      

def queryform(request,pk):
   print(pk) 
   data=Student.objects.get(id=pk)
   return render(request,'studash.html',{'data':data,'data1':data})


def querydata(request):
   if request.method=='POST':
     n=request.POST.get('name')
     e=request.POST.get('email')
     q=request.POST.get('query')    
     Query.objects.create(name=n,email=e,query=q)
     data=Student.objects.get(email=e)
     return render (request,'studash.html',{'data':data})
   

def allquery(request,pk):
   data=Student.objects.get(id=pk)
   email=data.email
   allquery=Query.objects.filter(email=email)
   return render(request,'studash.html',{'data':data,'allquery':allquery})



def delete(request,pk):
   delete_data=Query.objects.get(id=pk)
   email=delete_data.email
   delete_data.delete()
   data=Student.objects.get(email=email)
   allquery=Query.objects.filter(email=email)
   return render(request,'studash.html',{'data':data,'allquery':allquery})

def edit(request,pk):
   editdata=Query.objects.get(id=pk)
   email=editdata.email
   data=Student.objects.get(email=email)
   allquery=Query.objects.filter(email=email)
   return render(request,'studash.html',{'data':data,'allquery':allquery,'editdata':editdata})

def updatedata(request,pk):
   if request.method=="POST":
      x=Query.objects.get(id=pk)
      r=request.POST.get('query')
      email=request.POST.get('email')
      x.query=r
      x.save()
      data=Student.objects.get(email=email)
      allquery=Query.objects.filter(email=email)
      return render (request,'studash.html',{'data':data,'allquery':allquery})

def search(request,pk):
   if request.method=='POST':
      data=Student.objects.get(id=pk)
      email=data.email
      x=request.POST.get('search')
      # allquery=Query.objects.filter(query=x)
      allquery=Query.objects.filter(Q(email__exact=email)& Q(query__contains=x))
      return render (request,'studash.html',{'data':data,'allquery':allquery})



# def login(request):
#       if request.method=='POST':
#          email=request.POST.get('email')
#          password=request.POST.get('password')
#          # print(email,password)
#          user=Student.objects.filter(email=email).first()

           
#          if user is None:
#                messages.error(request, "Email is not registered")
#                return redirect("login")  # Redirect back to login page

#          # Check password (assuming plain text, but it's better to use hashed passwords)
#          if user.password == password:
#                return render(request, "admindash.html", {"data": user})
#          else:
#                messages.error(request, "Password does not match")
#                return redirect("login")

#       return render(request, "login.html")





      #    if user:
      #       data=Student.objects.get(email=email)  #extra line not need user me student ka object hai
      #       databasename=data.name
      #       databasepass=data.password
      #       if databasepass==password:
      #          return render(request,'admindash.html',{'data':data})    #{{data}}
      #       else:
      #          x="password is not match"
      #          return render(request,'home.html',{'msg':x})
      #    else:
      #       x="email does not register"
      #       return render(request,'home.html',{'msg':x})
      # else:
      #    return render(request,'login.html')
         
      


def registration(request):
    if request.method=='POST':
       name= request.POST.get('username')
       email= request.POST.get('email')
       discription= request.POST.get('Address')
       contact= request.POST.get('phone')
       dob= request.POST.get('dob')
       standard=request.POST.get('class')
       gender= request.POST.get('gender')
       image= request.FILES.get('Profile Picture')
    #    resume= request.FILES.get('resume')
       password = request.POST.get('password')
    #    cpassword= request.POST.get('cpassword')
    #    print(name,email,discription,contact,dob,edu,gender,image,resume,password,cpassword)
       user=Student.objects.filter(email=email)  # 
       if user:
          x="email already exist"
          return render (request,'registration.html',{'msg':x})
       else:
            Student.objects.create(name=name,email=email,standard=standard,phone=contact, gender=gender,dob= dob, profile_pic=image,address=discription,password=password)
            x="registration succesfully"
            return render(request,'home.html',{'msg':x})
    #       else:
    #          x="password and confirm password not match"
    #          return render(request,'registration.html',{'msg':x,'name':name,'email':email})
               
    else :   
     return render(request,'registration.html')


def admindash(request):
   
   context = {
         'student_count': Student.objects.count(),
         'teacher_count': Admin.objects.count(),
   }
   print("Students:", Student.objects.count())
   return render(request, 'admindash.html',context)

   #  return render(request,'admindash.html')
