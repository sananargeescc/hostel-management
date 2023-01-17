from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from pythonapp.forms import food_form, fee_form, payment_form, notification_form, attendance_form, staff_form, \
    hostel_form, replay_form, AddFee
from pythonapp.models import Food, Fee, Payment, Notification, Attendance, Staff, Hostel, Complaint, Booking, Review, \
    Student_Registration

@login_required(login_url='log')
def add_food(request):
    form = food_form()
    if request.method == "POST":
        form = food_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_food')
    return render(request, 'add_food.html', {'form': form})

@login_required(login_url='log')
def view_food(request):
    data = Food.objects.all()
    return render(request, 'food_details.html', {'data': data})

@login_required(login_url='log')
def add_fee(request):
    form = fee_form()
    if request.method == "POST":
        form = fee_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_fee')
    return render(request, 'add_fee.html', {'form': form})


#     form = AddFee()
#     if request.method == "POST":
#         form = AddFee(request.POST)
#         if form.is_valid():
#             bill = form.save(commit=False)
#             bill_qs=Fee.objects.filter(student=bill.student,from_date=bill.from_date,to_date=bill.to_date)
#             if bill_qs.exists():
#                 messages.info(request,'Bill Already added for the tudent in this duration')
#             else:
#                 bill.save()
#                 messages.info(request,'Bill Added')
#                 return redirect('add_fee')
#     return render(request, 'add_fee.html', {'form': form})
#
# @login_required(login_url='log')
# def load_bill(request):
#     student_id = request.GET.get('studentId')
#     from_date = request.GET.get('from_date')
#     to_date = request.GET.get('to_date')
#
#     student = Student_Registration.objects.get(user_id=student_id)
#     present_days = Attendance.objects.filter(student=student, date__range=[from_date, to_date]).count()
#     amount = present_days * 200
#     rent = 2000
#     data = {
#         'present_days': present_days,
#         'mess_bill': amount,
#         'room_rent': rent
#
#     }
#
#     return JsonResponse(data)



@login_required(login_url='log')
def view_fee(request):
    data = Fee.objects.all()
    return render(request, 'fee_details.html', {'data': data})

# @login_required(login_url='log')
# def view_payment(request):
#     payment = Fees.objects.filter(status=1)
#     return render(request, 'adminpages/view_payment.html', {'payments': payment})


@login_required(login_url='log')
def add_payment(request):
    form = payment_form()
    if request.method == "POST":
        form = payment_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_payment')
    return render(request, 'add_payment.html', {'form': form})

@login_required(login_url='log')
def view_payment(request):
    data = Payment.objects.all()
    return render(request, 'payment_details.html', {'data': data})

@login_required(login_url='log')
def add_notification(request):
    form = notification_form()
    if request.method == "POST":
        form = notification_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_notification')
    return render(request, 'add_notification.html', {'form': form})

@login_required(login_url='log')
def view_notification(request):
    data =Notification.objects.all()
    return render(request, 'notification_details.html', {'data': data})

@login_required(login_url='log')
def add_attendance(request):
    form = attendance_form()
    if request.method == "POST":
        form = attendance_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_attendance')
    return render(request, 'add_attendance.html', {'form': form})

@login_required(login_url='log')
def view_attendance(request):
    data = Attendance.objects.all()
    return render(request, 'attendance_details.html', {'data': data})

@login_required(login_url='log')
def add_staff(request):
    form = staff_form()
    if request.method == "POST":
        form = staff_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_staff')
    return render(request, 'add_staff.html', {'form': form})

@login_required(login_url='log')
def view_staff(request):
    data = Staff.objects.all()
    return render(request, 'staff_details.html', {'data': data})

@login_required(login_url='log')
def hostel_update(request,id):
    hostel1 = Hostel.objects.get(id=id)
    form = hostel_form(instance=hostel1)
    if request.method =='POST' :
        form=hostel_form(request.POST,request.FILES,instance = hostel1)
    if form.is_valid():
        form.save()
        return redirect('view_hostel')
    return render(request,'add_hostel.html',{'form':form})

@login_required(login_url='log')
def hostel_delete(request,id):
    Hostel.objects.get(id=id).delete()
    return redirect('view_hostel')

@login_required(login_url='log')
def food_update(request,id):
    food1 = Food.objects.get(id=id)
    form = food_form(instance=food1)
    if request.method =='POST' :
        form=food_form(request.POST,instance = food1)
    if form.is_valid():
        form.save()
        return redirect('view_food')
    return render(request,'add_food.html',{'form':form})

@login_required(login_url='log')
def food_delete(request,id):
    Food.objects.get(id=id).delete()
    return redirect('view_food')

@login_required(login_url='log')
def fee_update(request,id):
    fee1 = Fee.objects.get(id=id)
    form = fee_form(instance=fee1)
    if request.method =='POST' :
        form=fee_form(request.POST,instance = fee1)
    if form.is_valid():
        form.save()
        return redirect('view_fee')
    return render(request,'add_fee.html',{'form':form})

@login_required(login_url='log')
def fee_delete(request,id):
    Fee.objects.get(id=id).delete()
    return redirect('view_fee')

@login_required(login_url='log')
def payment_update(request,id):
    pay1 = Payment.objects.get(id=id)
    form = payment_form(instance=pay1)
    if request.method =='POST' :
        form=payment_form(request.POST,instance = pay1)
    if form.is_valid():
        form.save()
        return redirect('view_payment')
    return render(request,'add_payment.html',{'form':form})

@login_required(login_url='log')
def payment_delete(request,id):
    Payment.objects.get(id=id).delete()
    return redirect('view_payment')

@login_required(login_url='log')
def notification_update(request,id):
    notification1 = Notification.objects.get(id=id)
    form = notification_form(instance=notification1)
    if request.method =='POST' :
        form= notification_form(request.POST,instance =notification1)
    if form.is_valid():
        form.save()
        return redirect('view_notification')
    return render(request,'add_notification.html',{'form':form})

@login_required(login_url='log')
def notification_delete(request,id):
    Notification.objects.get(id=id).delete()
    return redirect('view_notification')

@login_required(login_url='log')
def attendance_update(request,id):
    attendance1 = Attendance.objects.get(id=id)
    form = attendance_form(instance=attendance1)
    if request.method =='POST' :
        form=attendance_form(request.POST,instance = attendance1)
    if form.is_valid():
        form.save()
        return redirect('view_attendance')
    return render(request,'add_attendance.html',{'form':form})

@login_required(login_url='log')
def attendance_delete(request,id):
    Attendance.objects.get(id=id).delete()
    return redirect('view_attendance')

@login_required(login_url='log')
def staff_update(request,id):
    staff1 = Staff.objects.get(id=id)
    form = staff_form(instance=staff1)
    if request.method =='POST' :
        form=staff_form(request.POST,instance = staff1)
    if form.is_valid():
        form.save()
        return redirect('view_staff')
    return render(request,'add_staff.html',{'form':form})

@login_required(login_url='log')
def staff_delete(request,id):
    Staff.objects.get(id=id).delete()
    return redirect('view_staff')

@login_required(login_url='log')
def view_complaint(request):
    data = Complaint.objects.all()
    return render(request, 'view_complaint.html', {'data': data})

@login_required(login_url='log')
def view_admin_booking(request):
    data = Booking.objects.all()
    return render(request, 'view_admin_booking.html', {'data': data})

@login_required(login_url='log')
def view_admin_review(request):
    data = Review.objects.all()
    return render(request, 'view_admin_review.html', {'data': data})

@login_required(login_url='log')
def complaint_replay(request,id):
    form = Complaint.objects.get(id=id)

    if request.method =='POST' :
         r = request.POST.get('replay')
         form.replay = r
         form.save()
         return redirect('view_complaint')
    return render(request,'replay_complaint.html',{'form':form})

@login_required(login_url='log')
def approve_booking(request,id):
    booking1 = Booking.objects.get(id=id)
    print(booking1)
    booking1.booking_status = 1
    booking1.save()
    messages.info(request,'Student Approved Successfully')
    return redirect(reverse('view_admin_booking'))

@login_required(login_url='log')
def reject_booking(request,id):
    booking1 = Booking.objects.get(id=id)
    # if request.method == 'POST':
    booking1.booking_status = 2
    booking1.save()
    messages.info(request, 'Rejected Student Registration')
    return redirect('view_admin_booking')

@login_required(login_url='log')
def view_logout(request):
    logout(request)
    return redirect('log')