from django.shortcuts import render
from django.http import HttpResponse
import pickle
from django.http import request,response
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.
def home(request):
    return render(request,'home.html')

def svm(request):
    return render(request,'svm.html')

def result(request):

    model = pickle.load(open("new_model.pickle", "rb"))
    lis = []
    lis.append(request.GET['a'])
    lis.append(request.GET['c'])
    lis.append(request.GET['d'])
    lis.append(request.GET['e'])
    lis.append(request.GET['f'])
    lis.append(request.GET['g'])
    lis.append(request.GET['h'])
    lis.append(request.GET['i'])
    lis.append(request.GET['j'])


    ans = model.predict([lis])
    
    if ans == [1]:
        ans = "Fraudulent Transaction"
    else:
        ans = "Non - Fraudulent Transaction"

    return render(request,'result.html',{'ans':ans})

def mail(request):
    
    send_mail(
        'credit card transacion details',
        ' The transcation is done successfully ',
        'anobhama08@gmail.com',
        ['anobhama99@gmail.com'],
        fail_silently=False,
    )

    return render(request,'mail.html')
