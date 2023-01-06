from django.shortcuts import render
from .models import department,booking,doctors,about
from .forms import bookingform,formsabout
#from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    if request.method == "POST":
        form = formsabout(request.POST)
        if form.is_valid():
            print("form is valid")
            form.save()
            return render(request, 'about.html',{'form':form})
        else:print("form not valid")

    form = formsabout
    dir = {'form': form}
    return render(request, 'about.html', dir)

def booking(request):
    if request.method == "POST":
        form = bookingform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form = bookingform()
    dirct_form = {'form': form}
    return render(request, 'booking.html',dirct_form)
def contact(request):
    return render(request, 'contact.html')
def depart(request,):
    dep = department.objects.all()
    return render(request, 'depart.html', {"dep": dep})
def doct(request):
    doc = {'doc': doctors.objects.all()}
    return render(request, 'doctors.html',doc)
def login(request):
    return render(request,'account form.html')