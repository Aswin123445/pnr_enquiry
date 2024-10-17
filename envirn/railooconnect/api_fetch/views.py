import json
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
from .services import fetch_data_from_api,custom_dictionary
from .data.pnr import datas
from .data.station import dit

# Create your views here.
def home_page(request):
    if request.method != 'GET' or request.GET.get('pnr') is None:
        return render(request,'homepage/home.html')
    pnr_number=request.GET.get('pnr')
    print(request.GET.get('pnr'))
    data=fetch_data_from_api(pnr_number)
    da=data.content.decode()
    dictionary_data = json.loads(da)  # Parse the string into a dictionary
    print(type(da))
    dictionary_data_needed=custom_dictionary(dictionary_data)
    for i in range(len(dit)):
        if dit[i]['code']==dictionary_data_needed['Sstation']:
            dictionary_data_needed['full_name'] = dit[i]['name']
        if dit[i]['code']==dictionary_data_needed['dstation']:
            dictionary_data_needed['destiation_name'] = dit[i]['name']
    print(dictionary_data_needed['Sstation'])
    print(dictionary_data_needed)
    context={'data':dictionary_data_needed,'height':22+(12*(dictionary_data_needed['numberpassenger']-1))}
    return render(request,'api_fetch/pnr.html',context)
def api_fetch(request):
   return render(request,'api_fetch/pnr.html',)


    
    
