from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def projecthomepage(request):
    return render(request, 'projecthomepage.html')

def artisthomepage(request):
    return render(request, 'artisthomepage.html')

def userhomepage(request):
    return render(request,'userhomepage.html')

def signup(request):
    return render(request,'signup.html')

def signup1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']
        if pass1 ==  pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'OOPS!,Username already taken.')
                return render(request,'signup.html')
            else:
                user = User.objects.create_user(username=username, password=pass1)
                user.save()
                messages.info(request,'Account created Successfully!')
                return render(request,'projecthomepage.html')

        else:
            messages.info(request,'Password does not match')
            return render(request,'signup.html')

def login(request):
    return render(request,'login.html')

def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user= auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request, user)
            if len(username)==10:
                return redirect('userhomepage')
            elif len(username)==4:
                return redirect('artisthomepage')
            else:
                return redirect('projecthomepage')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return render(request,'projecthomepage.html')

