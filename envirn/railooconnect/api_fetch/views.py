import json
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
from .services import fetch_data_from_api,custom_dictionary
# from .data.pnr import datas
from .data.station import dit
from django.views.decorators.cache import never_cache
from .models import PNR
from django.contrib.auth import get_user_model
from django.contrib import messages


# Create your views here.
@never_cache
def home_page(request):

    if 'user' not in request.session :
        return redirect('singin')
    if request.method != 'GET' or request.GET.get('pnr') is None:
        return render(request,'homepage/home.html')
    pnr_number=request.GET.get('pnr')
    data=fetch_data_from_api(pnr_number)
    if data is None or type(data) is str :
        messages.info(request , "pnr is flushed or not valid ")
        return render(request,'homepage/home.html')
    da=data.content.decode()
    dictionary_data = json.loads(da)  # Parse the string into a dictionary
    print(type(da))
    datas=custom_dictionary(dictionary_data)
    for i in range(len(dit)):
        if dit[i]['code'] == datas['Sstation']:
            datas['full_name'] = dit[i]['name']
        if dit[i]['code']==datas['dstation']:
            datas['destiation_name'] = dit[i]['name']
    print(datas['Sstation'])
    User=get_user_model()
    user_instance =  User.objects.get(id = request.user.id)
    pnr_instance=PNR.objects.create(
        user = user_instance,
        pnr = datas['pnr'],
        train_number = datas['train_number'],
        source_station = datas['Sstation'],
        destination_station = datas['dstation'],
        distance=datas['distance']      
    )
    context={'data':datas,'height':22+(12*(datas['numberpassenger']-1))}
    return render(request,'api_fetch/pnr.html',context)
def api_fetch(request):
   return render(request,'api_fetch/pnr.html')


    
    
