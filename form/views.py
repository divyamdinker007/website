from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.

def register(request):

    if request.method == 'POST':
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        password= request.POST['password']
        email= request.POST['email']
        username= request.POST['email']
        if password==password:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
            else:
                user = User.objects.create_user(username=username,password=password, email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('user created')
                return redirect('thankyou')
        else:
            messages.info(request, 'password not matching.....')
            return redirect('register')
        return redirect('index')

    else:    
        return render(request,'register.html')


def index(request):
    if request.method=='POST':
        email= request.POST.get('email')
        password= request.POST.get('password')

        user= auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('register')

        else:
            messages.info(request,'Invalid Info')
            return redirect('register')
    else:
        return render(request,'index.html')



def thankyou(request):
    return render(request, 'thankyou.html')
