from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
import datetime
from django import forms
import pytz
#from django.views.decorators.csrf import csrf_exempt



utc=pytz.UTC

def validator_link(linked):
    if len(str(linked)) > 5:# and len(str(obj)) == 0:
        error_list = ['ебаный рот как ты меня забела ошибка ебаная']
        raise ValidationError({'linked': linked})


def validator_password(obj):
    if len(str(obj)) > 10:
        raise ValidationError(
            ('Максимальная длинна пароля 10 символов'), 
            params={'password': obj})

def validator_limit(obj):
    if obj is not int and obj > 9999999 and obj < 0:
        raise ValidationError(
            ('Лимит должен быть положительным целочисленным значением, не более 9999999'), 
            params={'limit': obj})


def validator_descrip(obj):
    print(obj)
    if len(str(obj)) < 1000:
        raise ValidationError(
            ('Максимальная длинна описания 1000 символов. Для увеличения лимитов - обратитесь в поддержку'), 
            params={'description': obj})


#Влидаторы на время не работуют блять
"""def validator_datetime(obj):
    print(88888)
    print(str(type(obj)))
    print(88888)
    if 'datetime.datetime' not in str(type(obj)):
        forms.ValidationError("Headline must be more than 5 characters.")

def validator_datetime_stop(obj):
    
    if type(obj) == 'datetime.datetime' and obj > datetime.datetime.now():
        pass"""