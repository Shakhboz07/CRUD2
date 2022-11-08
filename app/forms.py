from django.forms import ModelForm

from app.models import Employee


class FormEmployee(ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'age', 'address', 'status', 'phone']
