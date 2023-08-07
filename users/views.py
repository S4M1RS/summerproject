from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def register(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')
        firstname = request.POST.get('first-name')
        lastname = request.POST.get('last-name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirm-password')

        print(username,firstname,lastname,email,password,confirmpassword)
        if password == confirmpassword:
            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=firstname,
                last_name=lastname,
                password=password,
            )
            user.save()
            return redirect("techhy:index")
        
    return render(request, "users/register.html")

def login(request):
    return render(request, "users/login.html")

def logout(request):
    print(request.user)
    return redirect(request, 'techhy:index')