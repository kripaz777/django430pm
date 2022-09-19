from django.shortcuts import render
from .models import *
# Create your views here.
def base():
    views = {}
    views['feedbacks'] = Feedback.objects.all()
    views['services'] = Service.objects.all()
    try:
        views['economy'] = Plan.objects.get().economy
        views['business'] = Plan.objects.get().business
        views['premium'] = Plan.objects.get().premium
        views['exclusive'] = Plan.objects.get().exclusive
    except:
        pass

    return views
def home(request):
    views = base()
    return render(request,'index.html',views)

def about(request):
    views = base()
    return render(request,'about.html',views)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        data = Contact.objects.create(name = name,email = email,subject = subject,message = message)
        data.save()
    return render(request,'contact.html')

def portfolio(request):
    return render(request,'portfolio.html')

def price(request):
    views = base()
    return render(request,'price.html',views)

def services(request):
    views = base()
    return render(request,'services.html',views)