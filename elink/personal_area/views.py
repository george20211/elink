from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from elink_index.models import LinkRegUser, InfoLink
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.views.decorators.cache import cache_page

def paginators(request, pages, count_pages):
    paginator = Paginator(pages, count_pages)
    paged = request.GET.get('page')
    return paginator.get_page(paged)


@login_required
#@cache_page(60 * 15)
def panel(request):
    user = request.user
    link_list = LinkRegUser.objects.filter(author=user)
    page = paginators(request, link_list, 1)
    context = {
        'page': page,
        'user': user,
    }
    return render(request, 'panel.html', context=context)

def link_id(request, id): #10-11
    link = get_object_or_404(LinkRegUser, id=id)
    if request.user == link.author or link.public_stat == True:
        device_stat = {
            1: 0,
            2: 0,
            3: 0,
        }
        time_stat = {
            '01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0, '08': 0,
            '09': 0, '10': 0, '11': 0, '12': 0, '13': 0, '14': 0, '15': 0, '16': 0,
            '17': 0, '18': 0, '19': 0, '20': 0, '21': 0, '22': 0, '23': 0, '24': 0,
        }
        stat = InfoLink.objects.filter(link_check=link)
        for data in stat:
            times_as_str = str(data.date_check)
            time_stat[f'{times_as_str[11:13]}'] += 1
            device_stat[data.device_id] += 1
        context = {
            'link': link,
            'time_stat': time_stat,
            'device_stat': device_stat,
        }
        return render(request, 'one_link_stat.html', context=context)
    else:
        return render(request, 'not_allowed.html')
