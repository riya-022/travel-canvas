from django.shortcuts import render
from .models import *
from django.contrib import messages
# Create your views here.

def registerpage(request):
    return render(request,"register.html")

def loginpage(request):
    return render(request,"login.html")

def showproductspage(request):
    return render(request,"showproducts.html")

def singleproductspage(request):
    return render(request,"singleproductspage")

def fetchregisterdata(request):
    # form to variable
    uname = request.POST.get("name")
    uemail = request.POST.get("email")
    uphone = request.POST.get("phone")
    upassword = request.POST.get("password")
    uaddress = request.POST.get("address")
    ugender = request.POST.get("gender")
    urole = request.POST.get("role")

    #for files

    uprofilepicture = request.FILES["dp"]

    print(uname)
    print(uphone)

    #insert query
    #INSERT INTO REGISTERMODEL(COLS NAME) VALUES()
    insertquery = registermodel(name=uname, email=uemail, phone=uphone, password=upassword, address=uaddress,
                                gender=ugender, role=urole, profilepicture=uprofilepicture)

    insertquery.save()
    print("success")

    return render(request, "register.html")

#login

def fetchlogindata(request):
    useremail = request.POST.get("email")
    userpassword = request.POST.get("password")

    print(useremail)
    print(userpassword)

    #select * from registermode1 where email=useremail and password=userpassword

    try:
        userdata = registermodel.objects.get(email=useremail, password=userpassword)
        print(userdata)
        print("success")

        request.session["log_id"] = userdata.id
        request.session["log_name"] = userdata.name
        request.session["log_email"] = userdata.email
    except:
        print("failure")
        userdata = None

    if userdata is not None:
        return render(request, "showproducts.html")
    else:
        print("invalid email or password")
        messages.error(request, "invalid email or password")

    return render(request, "login.html")

def logout(request):
    try:
        del request.session["log_id"]
        del request.session["log_name"]
        del request.session["log_email"]
    except:
        print("exception")
    return render(request, "showproducts.html")

def addproductpage(request):
    # query to fetch all category model data
    # select * from category

    catdata = category.objects.all()

    context = {
        "catdata": catdata
    }
    return render(request, "addproduct.html", context)
