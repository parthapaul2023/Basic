from django.http import HttpResponse
from django.shortcuts import redirect, render

def home(request):
    return HttpResponse("This is home page")

def about(request):
    return render(request,'about.html') 

def bootstrap(request):
    return render(request,'bootstrap.html')   

def register(request):
    a=5
    b='example'

    if (request.method=='POST'):
        email1=request.POST['email']
        password1=request.POST['password']
        print("Got data from register page: ",email1,password1)
        if(password1=='123456'):
            pass
        else:
           return redirect('/register') 
        return redirect('/about')
    return render(request,'register.html', {'test':a, 'test1':b})     