from django.contrib.auth.models import User
from django.shortcuts import render

from Hospitalapp.models import Department, Doctors,Booking1


# Create your views here.

def homepage(request):
    return render(request,'HomePage.html')

def aboutpage(request):
    return render(request,'AboutPage.html')

def departmentpage(request):
    department=Department.objects.all()
    context={'key1':department}
    return render(request,'DepartmentPage.html',context)

def doctorspage(request):
    doctors=Doctors.objects.all()
    context={'key2':doctors}
    return render(request, 'DoctorsPage.html', context)

def bookingpage(request):
    doctor = Doctors.objects.all()
    context = {'doctors':doctor}
    if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['number']
        doctor_name = Doctors.objects.get(id=request.POST['doctor_name'])
        email = request.POST['emails']
        date = request.POST['date']
        booking =Booking1.objects.create(patient_name=name,ph_number=number,doctor_name=doctor_name,booking_date=date,Email=email)
        booking.save();
    return render(request,'BookingPage.html',context)


