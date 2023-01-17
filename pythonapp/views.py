from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from pythonapp.forms import user_reg, Stud_form, parent_form, hostel_form
from pythonapp.models import Student_Registration, Parent_Registration, Hostel


# Create your views here.
def home(request):

    return render(request,'index.html')

def log(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('admin1')
            elif user is not None and user.is_student:
                if user.student.approval_status==True:
                    login(request,user)

                    return redirect('student')
            elif user.is_parent:
                if user.parent.approval_status==True:

                    login(request,user)

                    return redirect('parent')
        else:
            messages.info(request,'invalid credentials')

    return render(request,'login.html')

def stud_signup(request):
    u_form = user_reg()
    s_form = Stud_form()
    if request.method == 'POST':
        u_form = user_reg(request.POST)
        s_form = Stud_form(request.POST,request.FILES)
        if u_form.is_valid() and s_form.is_valid():
            user = u_form.save(commit=False)
            user.is_student = True
            user.save()
            student = s_form.save(commit=False)
            student.user = user
            student.save()
            messages.info(request,'student registered successfully')
            return redirect('log')

    return render(request,'signup.html',{'u_form':u_form,'s_form':s_form})

def parent_signup(request):
    u_form = user_reg()
    p_form = parent_form()
    if request.method == "POST":
        u_form = user_reg(request.POST)
        p_form = parent_form(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save(commit=False)
            user.is_parent = True
            user.save()
            parent = p_form.save(commit=False)
            parent.user = user
            parent.save()
            messages.info(request,'parent registered successfully')
            return redirect('log')
    return render(request,'parentsignup.html',{'u_form':u_form,'p_form':p_form})

@login_required(login_url='log')
def admin1(request):
    return render(request,'admin.html')

@login_required(login_url='log')
def student(request):
     return render(request,'student.html')

@login_required(login_url='log')
def parent(request):
    return render(request,'parent.html')

@login_required(login_url='log')
def view_student(request):
    data = Student_Registration.objects.all()
    return render(request, 'studentview.html', {'data': data})

@login_required(login_url='log')
def view_parent(request):
    data = Parent_Registration.objects.all()
    return render(request, 'parentview.html', {'data': data})

@login_required(login_url='log')
def approve_student(request,id):
    student = Student_Registration.objects.get(user_id=id)
    print(student)
    student.approval_status = 1
    student.save()
    messages.info(request,'Student Approved Successfully')
    return redirect(reverse('view_student'))

@login_required(login_url='log')
def reject_student(request,id):
    student = Student_Registration.objects.get(user_id=id)
    # if request.method == 'POST':
    student.approval_status = 2
    student.save()
    messages.info(request, 'Rejected Student Registration')
    return redirect('view_student')

@login_required(login_url='log')
def approve_parent(request,id):
    parent = Parent_Registration.objects.get(user_id=id)
    print(parent)
    parent.approval_status = 1
    parent.save()
    messages.info(request,'Student Approved Successfully')
    return redirect(reverse('view_parent'))

@login_required(login_url='log')
def reject_parent(request,id):
    parent = Parent_Registration.objects.get(user_id=id)
    # if request.method == 'POST':
    parent.approval_status = 2
    parent.save()
    messages.info(request, 'Rejected Student Registration')
    return redirect('view_parent')


@login_required(login_url='log')
def add_hostel(request):
    form = hostel_form()
    if request.method == "POST":
        form = hostel_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_hostel')
    return render(request,'add_hostel.html',{'form':form})

@login_required(login_url='log')
def view_hostel(request):
    data = Hostel.objects.all()
    return render(request, 'hostel_details.html', {'data': data})

