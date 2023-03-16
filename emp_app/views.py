from django.shortcuts import render, redirect
from .models import Employee, Role, Department
from datetime import datetime
from django.http import HttpResponse
from django.db.models import Q

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
    employee = Employee.objects.all()
    return render(request, 'remove_emp.html', context={'emps': employee})


def remove_single_emp(request, pk):
    single_emy = Employee.objects.get(id=pk)
    single_emy.delete()
    return redirect('remove_emp')


def filter_emp(request):

    all_department = Department.objects.all()
    all_role = Role.objects.all()
    emps = None
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            dept = int(request.POST.get('dept'))
            role = int(request.POST.get('role'))

            emps = Employee.objects.all()

            if name:
                if " " in name:
                    full_text = name.split()
                    emps = emps.filter(Q(first_name__icontains=full_text[0]))

                else:
                    emps = emps.filter(Q(first_name__icontains=name) | Q(
                        last_name__icontains=name))

            elif dept != 0:
                emps = emps.filter(dept__id=dept)
            elif role != 0:
                emps = emps.filter(role__id=role)
    except:
        emps = None

    return render(request, 'filter_emp.html', context={'all_dept': all_department, 'all_role': all_role, 'emps': emps})


def update_emp(request):
    employee = Employee.objects.all()

    return render(request, 'update.html', context={'emps': employee})


def single_update(request, pk):
    single_emp = Employee.objects.get(id=pk)
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

            single_emp.first_name = first_name
            single_emp.last_name = last_name
            single_emp.salary = salary
            single_emp.bonus = bonus
            single_emp.phone = phone
            single_emp.dept_id = dept
            single_emp.role_id = role

            single_emp.save()
            return redirect('update_emp')
    except:
        pass

    return render(request, 'updateForms.html', context={'form': single_emp, 'all_dept': all_department, 'all_role': all_role})
