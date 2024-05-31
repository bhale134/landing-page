from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import json
from datetime import datetime
from .gmail import envoi_mail
import threading
from .models import Client
# Create your views here.



def index(request):

    context ={}

    return render(request,'main/index.html',context)

def plan(request):

    context ={}

    return render(request,'main/plan.html',context)

def template(request):
    context ={}

    return render(request,'main/templates.html',context)

def register(request) :
    context = {}

    return render(request,'main/register.html',context)

def final_page(request):
    print(request)
    if(request.method == 'POST') :
        print(request.POST)
        nom = request.POST.get('nom')
        numero = request.POST.get('numero')
        email = request.POST.get('email')
        code_promo = request.POST.get('code')
        rue = request.POST.get('rue')
        ville = request.POST.get('ville')
        client = Client(
            nom=nom,
            numero=numero,
            email=email,
            code=code_promo,
            desc="",
            timestamp= datetime.now(),
            adresse = ville+ " "+rue,
         
        )
        
        client.save()

        
        t = threading.Thread(target=envoi_mail,args=(nom,email,numero,code_promo))
        t.start()
        
    context ={}

    return render(request,'main/final_page.html',context)


def politique(request):

    return render(request,"politique")
def service(request):

    return render(request,"service")