from django.contrib import admin

from pythonapp import models

# Register your models here.
admin.site.register(models.Login_view)
admin.site.register(models.Student_Registration)
admin.site.register(models.Parent_Registration)
admin.site.register(models.Attendance)
