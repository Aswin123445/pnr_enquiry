from django.http import JsonResponse
import requests
    

def fetch_data_from_api(pnr_number):
    url = f"https://irctc-indian-railway-pnr-status.p.rapidapi.com/getPNRStatus/{pnr_number}"
    header={
        'x-rapidapi-host': 'irctc-indian-railway-pnr-status.p.rapidapi.com',
        'x-rapidapi-key' : 'db7ea411f0msh9c7ce40ad6f5bf8p1ed4e9jsnf96f6c86c08e'
    }
    resonse=requests.get(url=url,headers=header) #
    print(resonse)
    return JsonResponse(resonse.json(),safe=False)

#creating custom dictonary
def custom_dictionary(data_dict):
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
    