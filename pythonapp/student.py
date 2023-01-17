from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from pythonapp.forms import complaint_form, review_form, booking_form, Stud_form, replay_form
from pythonapp.models import Hostel, Food, Fee, Notification, Attendance, Payment, Booking, Complaint, Review, \
    Student_Registration

@login_required(login_url='log')
def view_student_hostel(request):
    data = Hostel.objects.all()
    return render(request, 'student_view_hostel.html', {'data': data})

@login_required(login_url='log')
def view_student_food(request):
    data = Food.objects.all()
    return render(request, 'student_view_food.html', {'data': data})

@login_required(login_url='log')
def view_student_fee(request):
    data = Fee.objects.all()
    return render(request, 'student_view_fee.html', {'data': data})

@login_required(login_url='log')
def view_student_notification(request):
    data =Notification.objects.all()
    return render(request, 'student_view_notification.html', {'data': data})

@login_required(login_url='log')
def view_student_attendance(request):
    u= Student_Registration.objects.get(user=request.user)
    data=Attendance.objects.filter(student=u)
    return render(request, 'student_view_attendance.html', {'data': data})

@login_required(login_url='log')
def add_complaint(request):
    form = complaint_form()
    u = request.user
    if request.method == "POST":
        form = complaint_form(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            return redirect('view_student_complaint')
    return render(request, 'add_stud_complaint.html', {'form': form})

@login_required(login_url='log')
def view_student_complaint(request):
    data = Complaint.objects.filter(user=request.user)
    return render(request, 'student_view_complaint.html', {'data': data})


@login_required(login_url='log')
def view_student_payment(request):
    u = Student_Registration.objects.get(user=request.user)
    data = Payment.objects.filter(student_name=u)
    return render(request, 'student_view_payment.html', {'data': data})

def approve_payment(request,id):
    pay1 = Payment.objects.get(id=id)
    pay1.status = 1
    pay1.save()
    messages.info(request, 'Student paid Successfully')
    return redirect('view_student_payment')

def reject_payment(request,id):
    pay1 = Payment.objects.get(id=id)
    pay1.status = 2
    pay1.save()
    messages.info(request, 'Student not paid')
    return redirect('view_student_payment')


@login_required(login_url='log')
def add_review(request):
    form = review_form()
    if request.method == "POST":
        form = review_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_student_review')
    return render(request, 'add_review.html', {'form': form})

@login_required(login_url='log')
def view_student_review(request):
    u = Student_Registration.objects.get(user=request.user)
    data = Review.objects.filter(student_name=u)
    return render(request, 'student_view_review.html', {'data': data})


@login_required(login_url='log')
def add_student_booking(request):
    form = booking_form()
    if request.method == "POST":
        form = booking_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_student_booking')
    return render(request, 'add_stud_booking.html', {'form': form})

@login_required(login_url='log')
def view_student_booking(request):
    u = Student_Registration.objects.get(user=request.user)
    data = Booking.objects.filter(name=u)
    return render(request, 'stud_booking_details.html', {'data': data})

@login_required(login_url='log')
def student_booking_update(request,id):
    book1 = Booking.objects.get(id=id)
    form = booking_form(instance=book1)
    if request.method =='POST' :
        form=booking_form(request.POST,instance = book1)
    if form.is_valid():
        form.save()
        return redirect('view_student_booking')
    return render(request,'add_stud_booking.html',{'form':form})

@login_required(login_url='log')
def student_booking_delete(request,id):
    Booking.objects.get(id=id).delete()
    return redirect('view_student_booking')

@login_required(login_url='log')
def view_profile(request):
    student = Student_Registration.objects.get(user=request.user)
    return render(request,'view_profile.html',{'student':student})

@login_required(login_url='log')
def profile_update(request):
    stud1 = Student_Registration.objects.get(user=request.user)
    form = Stud_form(instance=stud1)
    if request.method =='POST' :
        form=Stud_form(request.POST,request.FILES,instance = stud1)
    if form.is_valid():
        form.save()
        return redirect('view_profile')
    return render(request,'update_profile.html',{'form':form})

# def account(request):
#
#     return render(request,'delete_acount.html')

# def confirm_delete(request):
#
#     return render(request,'confirm_delete.html')

@login_required(login_url='log')
def delete_account(request):
    user = request.user
    if request.method == 'POST':
        user.delete()
        messages.info(request, 'your Account Deleted Successfully')
        return redirect('log')
    return render(request, 'confirm_delete.html')

@login_required(login_url='log')
def cancel_confirm_delete(request):

    return redirect('view_profile')

@login_required(login_url='log')
def view_logout_student(request):
    logout(request)
    return redirect('log')