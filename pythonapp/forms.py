import datetime
import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from pythonapp.models import Student_Registration, Parent_Registration, Login_view, Hostel, Food, Fee, Payment, \
    Notification, Attendance, Staff, Complaint, Review, Booking

class DateInput(forms.DateInput):
    input_type = 'date'

def phone_number_validation(value):
    if not re.compile(r'^[7-9]\d{9}$').match(value):
        raise ValidationError('This is Not a Valid Phone Number')

class user_reg(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password',widget=forms.PasswordInput,)
    password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput,)
    class Meta:
        model = Login_view
        fields = ("username","password1","password2")


class Stud_form(forms.ModelForm):
    email = forms.CharField(validators=[RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9,_-]+\.[a-zA-Z]+$',message='Please Enter a Valid Email')])
    phone = forms.CharField(validators = [phone_number_validation])
    class Meta:
        model = Student_Registration
        exclude = ("user","approval_status",)

    def clean_email(self):
        mail = self.cleaned_data['email']
        parent_email = Parent_Registration.objects.filter(email=mail)
        student_email = Student_Registration.objects.filter(email=mail)
        if student_email.exists():
            raise forms.ValidationError("This Email already registered")
        if parent_email.exists():
            raise forms.ValidationError("This Email already registered")
        return mail

    def clean_phone(self):
        phone_number = self.cleaned_data['phone']
        parent_number = Parent_Registration.objects.filter(phone=phone_number)
        student_number = Student_Registration.objects.filter(phone=phone_number)
        if parent_number.exists():
            raise forms.ValidationError("This phone number already registered")
        if student_number.exists():
            raise forms.ValidationError("This phone number already registered")
        return phone_number

class parent_form(forms.ModelForm):
    email = forms.CharField(validators=[RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9,_-]+\.[a-zA-Z]+$', message='Please Enter a Valid Email')])
    phone = forms.CharField(validators=[phone_number_validation])
    class Meta:
        model =Parent_Registration
        exclude = ("user","approval_status",)

    def clean_email(self):
        mail = self.cleaned_data['email']
        parent_email = Parent_Registration.objects.filter(email=mail)
        student_email = Student_Registration.objects.filter(email=mail)
        if student_email.exists():
            raise forms.ValidationError("This Email already registered")
        if parent_email.exists():
            raise forms.ValidationError("This Email already registered")
        return mail

    def clean_phone(self):
        phone_number = self.cleaned_data['phone']
        parent_number = Parent_Registration.objects.filter(phone=phone_number)
        student_number = Student_Registration.objects.filter(phone=phone_number)
        if parent_number.exists():
            raise forms.ValidationError("This phone number already registered")
        if student_number.exists():
            raise forms.ValidationError("This phone number already registered")
        return phone_number


class hostel_form(forms.ModelForm):
    class Meta:
        model = Hostel
        fields = "__all__"

class food_form(forms.ModelForm):
    class Meta:
        model = Food
        fields = "__all__"

class AddFee(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = Fee
        fields = "__all__"


class fee_form(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = Fee
        fields = "__all__"


class payment_form(forms.ModelForm):
    from_date = forms.DateField(widget=DateInput)
    to_date = forms.DateField(widget=DateInput)
    class Meta:
        model = Payment
        fields = "__all__"
        exclude = ("status",)

class notification_form(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = Notification
        fields = "__all__"

att_choice = (
    ('present','present'),
    ('absent','absent')
)
class attendance_form(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    attendance_status = forms.ChoiceField(choices=att_choice,widget=forms.RadioSelect)
    class Meta:
        model = Attendance
        fields = "__all__"

class  staff_form(forms.ModelForm):
    phone = forms.CharField(validators=[phone_number_validation])
    class Meta:
        model = Staff
        fields = "__all__"

class  complaint_form(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = Complaint
        fields = "__all__"
        exclude = ("replay","user",)

class  replay_form(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = "__all__"
        exclude =("user","date","complaint",)


class  review_form(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"

class  booking_form(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    booking_date = forms.DateField(widget=DateInput)
    class Meta:
        model = Booking
        fields = "__all__"
        exclude = ("booking_status",)

# class AddFee(forms.ModelForm):
#     student = forms.ModelChoiceField(queryset=Student_Registration.objects.filter(approval_status=True))
#     from_date = forms.DateField(widget=DateInput)
#     to_date = forms.DateField(widget=DateInput)
#     room_rent = forms.CharField(
#         widget=forms.TextInput())
#     mess_bill = forms.CharField(
#         widget=forms.TextInput())
#     class Meta:
#         model = Fee
#         fields = ('student', 'from_date', 'to_date', 'room_rent', 'mess_bill')
#
#     def clean(self):
#         cleaned_data = super().clean()
#         from_date = cleaned_data.get("from_date")
#         to_date = cleaned_data.get("to_date")
#
#         if (from_date > datetime.date.today()):
#             raise forms.ValidationError("Invalid From Date")
#         if to_date <= from_date or to_date > datetime.date.today():
#             raise forms.ValidationError("Invalid To Date")
#
#         from_day = from_date.strftime("%d")
#         from_m = from_date.strftime("%m")
#         to_day = to_date.strftime("%d")
#         print(from_m, to_day)
#
#         if int(from_day) != 1:
#             raise forms.ValidationError('Invalid From Date')
#         if int(from_m) == 2:
#             if int(to_day) not in [29, 28]:
#                 raise forms.ValidationError('Invalid To Date')
#
#         else:
#
#             if int(from_m) in [1, 3, 5, 7, 8, 10, 12]:
#                 if int(to_day) != 31:
#                     raise forms.ValidationError('Invalid To Date')
#
#             elif int(from_m) == [4, 6, 9, 11]:
#
#                 if int(to_day) != 30:
#                     raise forms.ValidationError('Invalid To Date')
#
#         return cleaned_data
