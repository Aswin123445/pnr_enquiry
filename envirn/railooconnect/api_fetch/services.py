from django.http import JsonResponse
import requests
    

def fetch_data_from_api(pnr_number):
    url = f"https://irctc-indian-railway-pnr-status.p.rapidapi.com/getPNRStatus/{pnr_number}"
    header={
        'x-rapidapi-host': 'irctc-indian-railway-pnr-status.p.rapidapi.com',
        'x-rapidapi-key' : 'db7ea411f0msh9c7ce40ad6f5bf8p1ed4e9jsnf96f6c86c08e'
    }
    try:
        resonse=requests.get(url=url,headers=header)
        if resonse.status_code != 200:
            return 'pnr flushed or not genereated for the api'
        data=resonse.json()
        if data['success'] == True :
           return JsonResponse(data,safe=False)
    except requests.exceptions.RequestException as e:
        print(f'error occured while fetching data {e}') 
        return None   
    


#creating custom dictonary
def custom_dictionary(data_dict):
    if not data_dict:
        return False
    cust_dict={
        'train_name':data_dict['data']['trainName'],
        'train_number':data_dict['data']['trainNumber'],
        'pnr':data_dict['data']['pnrNumber'],
        'Sstation':data_dict['data']['sourceStation'],
        'dstation':data_dict['data']['destinationStation'],
        'numberpassenger':data_dict['data']['numberOfpassenger'],
        'chart_status':data_dict['data']['chartStatus'],
        'distance':data_dict['data']['distance'],
        'ticketFare':data_dict['data']['ticketFare'],
        'journey_compartment':data_dict['data']['journeyClass'],
        'quota':data_dict['data']['quota'],
        'passengerlist':[]
    }
    i=0
    while i < cust_dict['numberpassenger']:
        passenger_details={
            'booking_status':data_dict['data']['passengerList'][i]['bookingStatusDetails'],
            'current_status':data_dict['data']['passengerList'][i]['currentStatus'],
            'passengerSerialNumber':data_dict['data']['passengerList'][i]['passengerSerialNumber']
        }
        cust_dict['passengerlist'].append(passenger_details)
        i += 1
    return cust_dict
    