from django.urls import path

from pythonapp import views, admin1, student, parent

urlpatterns = [
          path('',views.home,name='home'),
          path('log',views.log,name='log'),
          path('stud_signup',views.stud_signup,name='stud_signup'),
          path('parent_signup',views.parent_signup,name='parent_signup'),
          path('admin1',views.admin1,name='admin1'),
          path('student',views.student,name='student'),
          path('parent',views.parent,name='parent'),
          path('view_student',views.view_student,name='view_student'),
          path('view_parent',views.view_parent,name='view_parent'),
          path('approve_student/<int:id>/',views.approve_student,name='approve_student'),
          path('reject_student/<int:id>/',views.reject_student,name='reject_student'),
          path('approve_parent/<int:id>/',views.approve_parent,name='approve_parent'),
          path('reject_parent/<int:id>/',views.reject_parent,name='reject_parent'),
          path('add_hostel',views.add_hostel,name='add_hostel'),
          path('view_hostel',views.view_hostel,name='view_hostel'),

          path('add_food',admin1.add_food,name='add_food'),
          path('view_food',admin1.view_food,name='view_food'),

          path('add_fee',admin1.add_fee,name='add_fee'),
          # path('ajax/load-bill/',admin1.load_bill,name='load_bill'),
          path('view_fee',admin1.view_fee,name='view_fee'),

          path('add_payment',admin1.add_payment,name='add_payment'),
          path('view_payment',admin1.view_payment,name='view_payment'),

          path('add_notification', admin1.add_notification, name='add_notification'),
          path('view_notification', admin1.view_notification, name='view_notification'),

          path('add_attendance', admin1.add_attendance, name='add_attendance'),
          path('view_attendance', admin1.view_attendance, name='view_attendance'),
          path('add_staff',admin1.add_staff,name='add_staff'),
          path('view_staff',admin1.view_staff,name='view_staff'),
          path('hostel_update/<int:id>/',admin1.hostel_update,name='hostel_update'),
          path('hostel_delete/<int:id>/',admin1.hostel_delete,name='hostel_delete'),
          path('food_update/<int:id>/',admin1.food_update,name='food_update'),
          path('food_delete/<int:id>/',admin1.food_delete,name='food_delete'),
          path('fee_update/<int:id>/',admin1.fee_update,name='fee_update'),
          path('fee_delete/<int:id>/',admin1.fee_delete,name='fee_delete'),
          path('payment_update/<int:id>/',admin1.payment_update,name='payment_update'),
          path('payment_delete/<int:id>/',admin1.payment_delete,name='payment_delete'),
          path('notification_update/<int:id>/',admin1.notification_update,name='notification_update'),
          path('notification_delete/<int:id>/',admin1.notification_delete,name='notification_delete'),
          path('attendance_update/<int:id>/',admin1.attendance_update,name='attendance_update'),
          path('attendance_delete/<int:id>/',admin1.attendance_delete,name='attendance_delete'),
          path('staff_update/<int:id>/',admin1.staff_update,name='staff_update'),
          path('staff_delete/<int:id>/',admin1.staff_delete,name='staff_delete'),
          path('view_student_hostel',student.view_student_hostel,name='view_student_hostel'),
          path('view_student_food',student.view_student_food,name='view_student_food'),
          path('view_student_fee',student.view_student_fee,name='view_student_fee'),
          path('view_student_notification',student.view_student_notification,name='view_student_notification'),
          path('view_student_attendance',student.view_student_attendance,name='view_student_attendance'),
          path('add_complaint',student.add_complaint,name='add_complaint'),
          path('view_student_complaint',student.view_student_complaint,name='view_student_complaint'),
          path('complaint_replay/<int:id>/', admin1.complaint_replay, name='complaint_replay'),

          path('view_student_payment',student.view_student_payment,name='view_student_payment'),
          path('approve_payment/<int:id>/',student.approve_payment,name='approve_payment'),
          path('reject_payment/<int:id>/',student.reject_payment,name='reject_payment'),


          path('add_review',student.add_review,name='add_review'),
          path('add_student_booking',student.add_student_booking,name='add_student_booking'),
          path('view_student_booking',student.view_student_booking,name='view_student_booking'),
          path('student_booking_update/<int:id>/', student.student_booking_update, name='student_booking_update'),
          path('student_booking_delete/<int:id>/', student.student_booking_delete, name='student_booking_delete'),
          path('view_complaint',admin1.view_complaint,name='view_complaint'),
          path('view_admin_booking',admin1.view_admin_booking,name='view_admin_booking'),
          path('view_admin_review',admin1.view_admin_review,name='view_admin_review'),
          path('view_student_review',student.view_student_review,name='view_student_review'),
          path('view_parent_hostel',parent.view_parent_hostel,name='view_parent_hostel'),
          path('view_parent_booking',parent.view_parent_booking,name='view_parent_booking'),
          path('view_parent_payment',parent.view_parent_payment,name='view_parent_payment'),
          path('view_parent_notification',parent.view_parent_notification,name='view_parent_notification'),
          path('view_parent_attendance',parent.view_parent_attendance,name='view_parent_attendance'),
          path('view_parent_staff',parent.view_parent_staff,name='view_parent_staff'),
          path('view_profile',student.view_profile,name='view_profile'),
          path('profile_update', student.profile_update, name='profile_update'),
          path('approve_booking/<int:id>/',admin1.approve_booking,name='approve_booking'),
          path('reject_booking/<int:id>/',admin1.reject_booking,name='reject_booking'),


          path('delete_account', student.delete_account, name='delete_account'),
          path('cancel_confirm_delete',student.cancel_confirm_delete,name='cancel_confirm_delete'),

          path('view_logout', admin1.view_logout, name='view_logout'),
          path('view_logout_student', student.view_logout_student, name='view_logout_student'),
          path('view_logout_parent', parent.view_logout_parent, name='view_logout_parent'),


          path('delete_account_parent', parent.delete_account_parent, name='delete_account_parent'),
          path('cancel_confirm_parent',parent.cancel_confirm_parent,name='cancel_confirm_parent'),





]