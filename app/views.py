from django.db.models import QuerySet
from django.shortcuts import render
import app.forms
from app.models import Employee


# Create your views here.
def home(request):
    return render(request,  'index.html')

def gallery(request):
        return render(request, 'gallery.html')

def aboutus(request):
    return render(request, 'about.html')


def contactus(request):
        return render(request,  'contact.html')

def join(request):
    if request.method == 'POST':
        form = app.EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'join.html')

    else:
        return render(request, 'join.html')

    def details(request):
        members: QuerySet[Employee] = Employee.objects.all()
        assert isinstance(members, object)
        return render(request, 'details.html', {'all': members})