from .models import LinkRegUser
from .forms import LinkpasswordForms
from django.shortcuts import render, redirect

class CheckLinks():

    def check_limited_link(request, obj):
        if obj.limit == True:
            if obj.limited_link >= 1:
                obj.limited_link = obj.limited_link - 1
                obj.save()
                return True
            else:
                return False
        return 'Unlimit'