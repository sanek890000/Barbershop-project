from django import forms
from .models import Visit

class VisitForm(forms.ModelForm):
       class Meta:
           model = Visit
           fields = ['name', 'phone', 'master', 'service']
       def __init__(self, *args, **kwargs):
           super().__init__(*args, **kwargs)
           self.fields['master'].empty_label = "Выберите мастера"
           self.fields['service'].empty_label = "Выберите услугу"