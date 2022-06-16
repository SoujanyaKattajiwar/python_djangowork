from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from conceptapp.models import Employee, Department, Role
import datetime


# Create your views here.
def index(request):
    return render(request, 'index.html')


def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'all_emp.html', context)


def add_emp(request):
    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        # hire_date = request.POST['hire_date']
        new_emp = Employee(first_name=first_name,
                           last_name=last_name,
                           salary=salary,
                           dept_id=dept,
                           role_id=role,
                           bonus=bonus,
                           phone=phone,
                           hire_date=datetime.datetime.now())
        new_emp.save()
        return HttpResponse("Employee Added Successfully")
    elif request.method == 'GET':
        return render(request, 'add_emp.html')

    else:
        return HttpResponse("An Exception occurred Employee has not added")


def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Empoyee Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    emps = Employee.objects.all()
    context = {
        'emps': emps

    }

    return render(request, 'remove_emp.html', context)


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(
                Q(first_name__icontains=name) | Q(last_name__icontains=name))  # icontains means ignore casesenstive
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__name__icontains=role)

        context = {
            'emps': emps
        }
        return render(request, 'all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse("An Exception Occured")
    return render(request, 'filter_emp.html', )
