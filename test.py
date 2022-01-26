import requests
import json

client_id = '0feca865-844a-4260-939a-a725430e72cc'

endpoint = 'https://frost.met.no/observations/v0.jsonld'
parameters = {
    'sources': 'SN18700,SN90450',
    'elements': 'mean(air_temperature P1D),sum(precipitation_amount P1D),mean(wind_speed P1D)',
    'referencetime': '2010-04-01/2010-04-03',
}
# Issue an HTTP GET request
r = requests.get(endpoint, parameters, auth=(client_id,''))
# Extract JSON data
json1 = r.json()

if r.status_code == 200:
    data = json1['data']
    print('Data retrieved from frost.met.no!')
else:
    print('Error! Returned status code %s' % r.status_code)
    print('Message: %s' % json1['error']['message'])
    print('Reason: %s' % json1['error']['reason'])

with open('data.txt', 'w') as f:
    json.dump(data, f)
