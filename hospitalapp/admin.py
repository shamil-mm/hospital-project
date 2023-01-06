from django.contrib import admin
from .models import department, booking,doctors,about
# Register your models here.
class departmentadmin(admin.ModelAdmin):
    list_display = ('dep_name','dep_description')
admin.site.register(department,departmentadmin)


class doctorsadmin(admin.ModelAdmin):
    list_display = ('dr_name','dr_spec','dep_name','dr_image','dep_description')
admin.site.register(doctors,doctorsadmin)



class bookingadmin(admin.ModelAdmin):
    list_display = ('p_name','p_phone','p_email','booking_date')
admin.site.register(booking,bookingadmin)

class aboutadmin(admin.ModelAdmin):
    list_dispay = ("first_name",'last_name',"phone_number",'password','re_password')
admin.site.register(about,aboutadmin)


