from django.shortcuts import render
from .gmail import envoi_mail
import threading
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
        t = threading.Thread(target=envoi_mail,args=(nom,email,numero,code_promo))
        t.start()
        
    context ={}

    return render(request,'main/final_page.html',context)


def politique(request):

    return render(request,"politique")
def service(request):

    return render(request,"service")