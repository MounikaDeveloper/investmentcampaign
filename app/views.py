from django.shortcuts import render, redirect
from django.contrib import messages
from app.models import InvestmentLoginModel
# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def saveLogin(request):
    name=request.POST['name']
    email = request.POST['email']
    mobile = request.POST['mobile']
    login=InvestmentLoginModel(name=name,emailid=email,mobile_no=mobile)
    login.save()
    messages.success(request, 'Login Successful')
    return redirect('index')