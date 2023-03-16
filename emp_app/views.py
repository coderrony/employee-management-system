from django.shortcuts import render, redirect
from .models import Employee, Role, Department
from datetime import datetime
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')


def all_emp(request):
    employee = Employee.objects.all()

    return render(request, 'all_emp.html', context={'emps': employee})


def add_emp(request):

    all_department = Department.objects.all()
    all_role = Role.objects.all()
    try:
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            salary = int(request.POST.get('salary'))
            bonus = int(request.POST.get('bonus'))
            phone = int(request.POST.get('phone'))
            dept = int(request.POST.get('dept'))
            role = int(request.POST.get('role'))

            new_employee = Employee(first_name=first_name, last_name=last_name, dept_id=dept,
                                    salary=salary, bonus=bonus, role_id=role, phone=phone, hire_date=datetime.now())
            new_employee.save()
            return redirect('all_emp')
    except:
        pass

    return render(request, 'add_emp.html', context={'all_dept': all_department, 'all_role': all_role})


def remove_emp(request):
    return render(request, 'remove_emp.html')


def filter_emp(request):
    return render(request, 'filter_emp.html')
