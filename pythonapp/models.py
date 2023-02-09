from django.contrib.auth.models import AbstractUser
from django.db import models



# Create your models here.
class Login_view(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)


class Student_Registration(models.Model):
    user = models.OneToOneField(Login_view,on_delete=models.CASCADE,related_name='student',null=True)
    name=models.CharField(max_length=200)
    registration_id=models.CharField(max_length=25)
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.CharField(max_length=200)
    approval_status = models.IntegerField(default=0)
    student_image = models.ImageField(upload_to='image')

    def __str__(self):
        return self.name

class Parent_Registration(models.Model):
    user = models.OneToOneField(Login_view, on_delete=models.CASCADE,null=True,related_name='parent')
    parent_name=models.CharField(max_length=200)
    student_name=models.ForeignKey(Student_Registration,on_delete=models.CASCADE)
    registration_id=models.CharField(max_length=25)
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.CharField(max_length=200)
    approval_status = models.IntegerField(default=0)

    def __str__(self):
        return self.parent_name

class Hostel(models.Model)  :
    hostel_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    Fee_details = models.CharField(max_length=25)
    total_rooms = models.IntegerField()
    room_fecilities = models.CharField(max_length=200)
    contact_number = models.IntegerField()
    hostel_image = models.ImageField(upload_to='image')

    def __str__(self):
        return self.hostel_name

class Food(models.Model):
    breakfast = models.CharField(max_length=200)
    Lunch = models.CharField(max_length=200)
    evening_snacks = models.CharField(max_length=200)
    dinner = models.CharField(max_length=200)

    def __str__(self):
        return self.breakfast

class Fee(models.Model):
    hostel_name = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    room_rent = models.FloatField()
    mess_bill = models.FloatField()
    amount = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return self.room_rent

class Payment(models.Model):
    student_name = models.ForeignKey(Student_Registration,on_delete=models.CASCADE)
    room_rent = models.IntegerField()
    mess_bill = models.IntegerField()
    amount = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()
    status = models.IntegerField(default=0)



    def __str__(self):
        return self.student_name


class Notification(models.Model):
    date = models.DateTimeField()
    add_message = models.TextField(max_length=200)


    def __str__(self):
        return self.date


class Attendance(models.Model):
    date= models.DateField()
    student = models.ForeignKey(Student_Registration,on_delete=models.DO_NOTHING)
    attendance_status = models.CharField(max_length=200)


    def __str__(self):
        return self.attendance_status


class Staff(models.Model):
    staff_name = models.CharField(max_length=200)
    phone = models.IntegerField()
    address = models.CharField(max_length=200)


    def __str__(self):
        return self.staff_name


class Complaint(models.Model):
    user = models.ForeignKey(Login_view, on_delete=models.DO_NOTHING)
    date = models.DateTimeField()
    complaint = models.CharField(max_length=1200)
    replay = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.user



class Review(models.Model):
    student_name = models.ForeignKey(Student_Registration, on_delete=models.DO_NOTHING)

    review = models.TextField(max_length=1200)


    def __str__(self):
        return self.student_name


class Booking(models.Model):
    name = models.ForeignKey(Student_Registration, on_delete=models.DO_NOTHING)

    booking_date = models.DateField()
    joining_date = models.DateField()
    booking_status = models.IntegerField(default=0)


    def __str__(self):
        return self.name


