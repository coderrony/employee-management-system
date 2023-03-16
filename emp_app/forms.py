from django.forms import ModelForm
from .models import Employee


class DetailsUpdate(ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name']
