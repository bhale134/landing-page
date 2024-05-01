from django.shortcuts import render
from .gmail import envoi_mail
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
        age = request.POST.get('nom')
        envoi_mail(nom,email,numero)
    context ={}

    return render(request,'main/final_page.html',context)


