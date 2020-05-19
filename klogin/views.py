from django.shortcuts import render,redirect
from .models import Registration
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse



# Create your views here.

# def first_page(request):
#     return render(request, "first_page.html")


def signup(request):
    return render(request, "signup.html")


def save(request):
    if request.method == "POST":
        username = request.POST["uname"]
        first_name = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["confirm_password"]

        dob = request.POST["dob"]
        phone = request.POST["phone"]

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username Taken")
            return render(request, "signup.html")
        elif password != password2:
            messages.info(request, "Password not matching")
            return render(request, "signup.html")
        elif User.objects.filter(email=email).exists():
            messages.info(request, "Email already exists")
            return render(request, "signup.html")
        else:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name,
                                            last_name=lname)
            print("user created")
            user.save()
            profile_obj = Registration(one_2_one=user,dob=dob, phone=phone)

            # profile.dob=dob
            # profile.phone=phone
            profile_obj.save()

            return redirect("/")

    else:
        return HttpResponse("ERROR!!")


def signin(request):

    if request.method == "POST":
        username = request.POST["uname"]
        password = request.POST["password"]

        user=auth.authenticate(username=username, password=password)

        if user is not None:
            print("user exists")
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"invalid credentials")
            return redirect("signin")
    else:
        return render(request,"signin.html")

#        enc_password=pbkdf2_sha256.encrypt(password,rounds=12000,salt_size=32)
#        user.password=enc_password


def logout(request):
    auth.logout(request)
    print("User logout")
    return redirect("/")


def profile(request):
    registration=Registration.objects.get(one_2_one=request.user)
    return render(request,"profile.html",{"registration":registration})

# or we can use link to send name and we can print data**
