from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from pythonapp.forms import parent_form
from pythonapp.models import Hostel, Booking, Notification, Attendance, Staff, Payment, Parent_Registration

@login_required(login_url='log')
def view_parent_hostel(request):
    data = Hostel.objects.all()
    return render(request, 'parent_view_hostel.html', {'data': data})

@login_required(login_url='log')
def view_parent_booking(request):
    u = Parent_Registration.objects.get(user=request.user)
    data = Booking.objects.filter(name=u.student_name)
    return render(request, 'parent_view_booking.html', {'data': data})

@login_required(login_url='log')
def view_parent_payment(request):
    u = Parent_Registration.objects.get(user=request.user)
    data = Payment.objects.filter(student_name=u.student_name)
    return render(request, 'parent_view_payment.html', {'data': data})

@login_required(login_url='log')
def view_parent_notification(request):
    data = Notification.objects.all()
    return render(request, 'view_parent_notification.html', {'data': data})

@login_required(login_url='log')
def view_parent_attendance(request):
    u=Parent_Registration.objects.get(user=request.user)
    data = Attendance.objects.filter(student=u.student_name)
    return render(request, 'parent_view_attendance.html', {'data': data})

@login_required(login_url='log')
def view_parent_staff(request):
    data = Staff.objects.all()
    return render(request, 'parent_view_staff.html', {'data': data})

@login_required(login_url='log')
def view_logout_parent(request):
    logout(request)
    return redirect('log')

@login_required(login_url='log')
def delete_account_parent(request):
    user = request.user
    if request.method == 'POST':
        user.delete()
        messages.info(request, 'your Account Deleted Successfully')
        return redirect('log')
    return render(request, 'delete_parent_profile.html')

@login_required(login_url='log')
def cancel_confirm_parent(request):

    return redirect('parent')


