__all__ = {'time', 'valuate', 'model_form_upload', 'result'}

import requests

from django.shortcuts import render, redirect

from .forms import DocumentForm




#def time(request):

    #city_1 = 'Berlin'
    #city_2 = 'London'
    #city_3 = 'Minsk'

    #url_city_1 = f'http://worldtimeapi.org/api/timezone/Europe/{city_1}'
    #url_city_2 = f'http://worldtimeapi.org/api/timezone/Europe/{city_2}'
    #url_city_3 = f'http://worldtimeapi.org/api/timezone/Europe/{city_3}'

    #res_1 = requests.get(url=url_city_1).json()
    #res_2 = requests.get(url_city_2).json()
    #res_3 = requests.get(url_city_3).json()

    #city_info_1 = {'city': city_1,
    #                'time': res_1['datetime'][11:19]}
    #city_info_2 = {'city': city_2,
    #                'time': res_2['datetime'][11:19]}
    #city_info_3 = {'city': city_3,
    #                'time': res_3['datetime'][11:19]}

    #context = {'info_berlin': city_info_1,
    #           'info_london': city_info_2,
    #           'info_minsk': city_info_3}

    #return context


def valuate(request):
    usd_id = '145'
    eur_id = '292'
    rub_id = '298'

    usd_url = f'http://www.nbrb.by/API/ExRates/Rates/{usd_id}'
    eur_url = f'http://www.nbrb.by/API/ExRates/Rates/{eur_id}'
    rub_url = f'http://www.nbrb.by/API/ExRates/Rates/{rub_id}'

    usd_res = requests.get(usd_url).json()
    eur_res = requests.get(eur_url).json()
    rub_res = requests.get(rub_url).json()

    usd_info = {'valuate': usd_res['Cur_Abbreviation'],
                'score': usd_res['Cur_OfficialRate']}
    eur_info = {'valuate': eur_res['Cur_Abbreviation'],
                'score': eur_res['Cur_OfficialRate']}
    rub_info = {'valuate': rub_res['Cur_Abbreviation'],
                'score': rub_res['Cur_OfficialRate']}

    context = {'info_1': usd_info,
               'info_2': eur_info,
               'info_3': rub_info, }
    return context


def model_form_upload(request):
    context = {}
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
        context = {'form': form}
    return  context


def result(request):
    context = {'res_upload': model_form_upload(request),
               'res_valuate': valuate(request), }
#              'res_1': time(request)
    return render(request=request, template_name='clock.html', context=context)


