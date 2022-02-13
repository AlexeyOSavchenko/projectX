import requests
import json

client_id = '0feca865-844a-4260-939a-a725430e72cc'

sources_endpoint = 'https://frost.met.no/sources/v0.jsonld'
sources_parameters = {'ids': 'SN*', 'country': 'NO'}

observations_endpoint = 'https://frost.met.no/observations/v0.jsonld'
observations_parameters = {'sources': 'SN18700,SN90450', 'elements': 'mean(wind_speed P1D)', 'referencetime': '2010-04-01/2020-04-03'}

def get_data(endpoint, parameters):
    responce = requests.get(endpoint, parameters, auth=(client_id, ''))
    if responce.status_code == 200:
        print('Data retrieved from frost.met.no!')
    else:
        print('Error! Returned status code %s' % responce.status_code)
    json_data = responce.json()
    return json_data

print(get_data(sources_endpoint, sources_parameters))
print(get_data(observations_endpoint, observations_parameters))