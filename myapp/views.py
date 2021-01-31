from django.shortcuts import render,HttpResponse
from myapp.models import Contact
from myapp.models import Product
from django.contrib import messages
# Create your views here.
def index(request):
    products= Product.objects.all()
    params={'products':products}
    return render(request,'index.html',params)
def about(request):
    return render(request,'about.html')
def cars(request):
    products= Product.objects.all()
    params={'products':products}
    return render(request,'cars.html' , params)
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact=Contact(name=name,email=email,subject=subject,message=message)
        contact.save()
        messages.success(request,"Your details have been submitted successfully.")

    return render(request,'contact.html')
def carDetails(request,myid):
    product=Product.objects.filter(id=myid)
    return render(request,"car-details.html",{'product':product[0]})