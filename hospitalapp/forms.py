from django import forms
from .models import booking,about


class dateinput(forms.DateInput):
    input_type = 'date'

class bookingform(forms.ModelForm):
    class Meta:
        model = booking
        fields = "__all__"
        widgets = {
            'booking_date':dateinput(),

        }
        labels = {
            'p_name':"Patient Name",
            'p_phone':"Patient Phone",
            'p_email':"Patient email",
            'dr_name':"Doctor Name",
            'booking_date':"Booking Date",
        }
class formsabout(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        f_name = self.cleaned_data.get("first_name")
        l_name = self.cleaned_data.get("last_name")
        p_number = self.cleaned_data.get("phone_number")
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")
        if f_name[0] !="s":
            raise forms.ValidationError(" Name must start with s ")
        elif password != re_password :
            raise forms.ValidationError("password must be same")

    class Meta:
        model = about
        fields = "__all__"
