from email.policy import default
from django import forms
import datetime
from django.forms import ModelForm
from .validators import (validator_link)
from elink_index.models import LinkRegUser
from django.core.validators import URLValidator


class LinkregForms(forms.Form):

    linked = forms.CharField(max_length=5000)
    description = forms.CharField(required=False)# validators=[validator_descrip], 
    limited_link = forms.IntegerField(required=False, max_value=9999999) # validators=[validator_limit], 
    secure_link = forms.CharField(max_length=10, min_length=0, required=False) # validators=[validator_password]
    start_link = forms.DateTimeField(#validators=[validator_datetime],
                                     required=False,
                                     widget=forms.DateInput(attrs={'type': 'datetime-local'}),
                                     initial=datetime.date.today(), localize=False)
    date_stop = forms.DateTimeField(#validators=[validator_datetime], 
                                    required=False,
                                    widget=forms.DateInput(attrs={'type': 'datetime-local'}),
                                    initial=datetime.date.today(), localize=False)
    #limit = forms.BooleanField(required=False, initial=False)


"""class LinkregForms(ModelForm):
    





validator_password,
                         validator_limit,
                         validator_link,
                         validator_descrip,
                         validator_datetime,
                         







    linked = forms.CharField()

    class Meta:
        model = LinkRegUser
        fields = ['linked', 'description', 'limited_link', 'secure_link', 'start_link', 'date_stop']
    
    def clean_linked(self):
        linked = self.cleaned_data.get('linked', False)
        if linked == False:
            print(4444444444444444444444444444444444444444444444444444444444444444444444444)
            raise ValueError('Error')
        else:
            print(44444444444444444444444444444444444444444444444444444444444444444444444447)
            print(linked)
            print(linked.replace(' ', ''))
            return linked.replace(' ', '')"""



class LinkdontregForms(forms.Form):

    linked = forms.CharField(max_length=5000, min_length=1)#validators=[validator_link]

class LinkpasswordForms(forms.Form):

    secure_link = forms.CharField(max_length=10, min_length=0) #validators=[validator_password]