from datetime import datetime
import redis
import pytz
import os
import time
import validators
from .checks import CheckLinks as CL
from .get_country import DetectCountry as DC
from .generator_url import GeneratorUrl as GU
from .qr_generator import QrcodeGenerator as QG
from .forms import LinkregForms, LinkpasswordForms
from .models import InfoLink, LinkRegUser
from users.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.utils import timezone
from django.http import HttpResponse
from django.template.response import TemplateResponse

redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT,
                                   db=0)
utc=pytz.UTC
one_week = 604800

def index(request):
    form = LinkregForms()
    if request.method == 'POST':
        if request.user.is_anonymous:
            form = LinkregForms(request.POST)
            print(form)
            if form.is_valid():
                linked_link = GU.generators_url_redis()
                #linked = form.cleaned_data.update("linked", False)
                linked = form.cleaned_data.get('linked')
                redis_instance.set(linked_link[22:], linked)
                form.reply = linked_link
                print(form.reply)
                print(form.reply)
                print(form.reply)
                print(form.reply)
                print(form.reply)
                context = {
                    'form': form,
                    'qr': QG.get_qr_code(linked_link),#get_qr_code(linked_link),
                    'qrcode': True
                }
                return render(request, 'index.html', context=context)
            else:
                print('не валидно на входе')
        else:
            form = LinkregForms(request.POST)
            if form.is_valid():
                linked_link = GU.generators_url()
                code_link = linked_link[22:]
                author = get_object_or_404(User, id=request.user.id)
                limited_link = form.cleaned_data.get('limited_link')
                linked = form.cleaned_data.get('linked')
                object_url = validators.url(linked, public=False)
                if object_url is not True:
                    return render(request, 'error_url.html')
                if type(limited_link) == int:
                    try:
                        LinkRegUser.objects.create(**form.cleaned_data,
                                                   linked_link=code_link,
                                                   author=author, limit=True)
                    except IntegrityError:
                        linked_link = linked_link[22:]
                        update_link = GU.generators_url()
                        linked_link += update_link[22:]
                        LinkRegUser.objects.create(**form.cleaned_data,
                                                   linked_link=linked_link,
                                                   author=author, limit=True)
                else:
                    try:
                        LinkRegUser.objects.create(**form.cleaned_data,
                                                   linked_link=code_link,
                                                   author=author)
                    except:
                        update_url = GU.generators_url()
                        code_link_2 = update_url[22:]
                        code_link = code_link + code_link_2
                        linked_link += code_link_2
                        LinkRegUser.objects.create(**form.cleaned_data,
                                                   linked_link=code_link,
                                                   author=author)
                form.reply = linked_link
                context = {
                    'form': form,
                    'qr': QG.get_qr_code(linked_link),
                    'qrcode': True
                }
                return render(request, 'index.html', context=context)
            return 'форма не валидна'
    context = {
        'form': form
        }
    return render(request, 'index.html', context=context)

def open_link(request, linkeds):
    if 'R' in linkeds:
        try:
            data = redis_instance.get(linkeds).decode('UTF-8')
            return redirect(data)
        except AttributeError:
            return render(request, 'not_found_link.html')
        except IndexError:
            return render(request, 'not_found_link.html')
    if 'P' in linkeds:
        #rep.set_cookie(key,value)
        try:
            obj = LinkRegUser.objects.get(linked_link=linkeds)
            now = timezone.now()
            if obj.start_link is not None and obj.start_link > now:
                return render(request, 'not_time.html')
            if obj.date_stop is not None and obj.date_stop < now:
                return render(request, 'end_time.html')
            if obj.secure_link != '':
                form = LinkpasswordForms()
                form.linked = obj.linked_link
                context = {
                    'form': form
                    }
                return render(request, 'secure_link.html', context=context)
            device_name = request.META['HTTP_USER_AGENT']
            if ('Windows' or 'Linux' or 'Macintosh' or 'Dos') in device_name:
                device_id = 1 #ПК будет
            elif ('Android' or 'ios') in device_name:
                device_id = 2#Мобильные
            else:
                device_id = 404#Не удалось определить
            limit = CL.check_limited_link(request, obj)   #Если лимит переходов кончился False, если нет True, если лимитов нет 'Unlimit'
            #print(answer)
            if limit == True:
                country = DC.get_client_ip(request)
                date_check = time.strftime("%Y-%m-%d %H:%M")
                if f'{obj.linked_link}' in request.COOKIES:
                    obj.how_many_link += 1
                    obj.again_how_many_link += 1
                    obj.save()
                else:
                    obj.how_many_link += 1
                    obj.save()
                    InfoLink.objects.create(link_check=obj, country_check_id=country, date_check=date_check, device_id=device_id)
                response = TemplateResponse(request, 'redirect.html', { 'site': obj.linked })
                response.set_cookie(f'{obj.linked_link}', max_age=one_week)
                #return render(request, 'redirect.html', { 'site': obj.linked })
                return response
            elif limit == False:
                return render(request, 'limit_end.html')
            else:
                country = DC.get_client_ip(request)
                date_check = time.strftime("%Y-%m-%d %H:%M")
                InfoLink.objects.create(link_check=obj, country_check_id=country, date_check=date_check, device_id=device_id)
                return redirect(obj.linked)
        except ObjectDoesNotExist:
            return render(request, 'not_found_link.html')
    else:
        return render(request, 'not_found_link.html')

def open_secure_link(request, linkeds):
    obj = LinkRegUser.objects.get(linked_link=linkeds)
    context = {}
    if request.method == 'POST':
        form = LinkpasswordForms(request.POST)
        if form.is_valid():
            password_link = form.cleaned_data.get("secure_link")
            if obj.secure_link == password_link:
                answer = CL.check_limited_link(request, obj)
                if answer == True:
                    return redirect(obj.linked)
                else:
                    return render(request, 'limit_end.html')
            else:
                context['bad_key'] = True
        else:
            print('Какая то хуйня с формой для пароля')
    form = LinkpasswordForms()
    form.linked = obj.linked_link
    context['form'] = form
    return render(request, 'secure_link.html', context=context)
