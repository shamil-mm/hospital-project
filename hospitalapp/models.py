from django.db import models

# Create your models here.
class department (models.Model):
    dep_name = models.CharField(max_length=255)
    dep_description = models.TextField()
    def __str__(self):

            return f"{ self.dep_name } - { self.dep_description }"

class doctors(models.Model):
    dr_name = models.CharField(max_length=255)
    dr_spec = models.CharField(max_length=255)
    dep_name = models.ForeignKey(department, on_delete=models.CASCADE,related_name='d_name')
    dep_description = models.ForeignKey(department, on_delete=models.CASCADE,related_name='d_description',default="hey")
    dr_image = models.ImageField(upload_to='doctors')

    def __str__(self):
        return "Dr."+self.dr_name+" "+self.dr_spec


class booking(models.Model):
    p_name = models.CharField(max_length=255)
    p_phone = models.CharField(max_length=10)
    p_email = models.EmailField()
    dr_name = models.ForeignKey(doctors, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)

class about(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    password = models.CharField(max_length=5)
    re_password = models.CharField(max_length=5)