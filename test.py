import requests
import json

client_id = '0feca865-844a-4260-939a-a725430e72cc'

sources_endpoint = 'https://frost.met.no/sources/v0.jsonld'
sources_parameters = {'ids': 'SN*', 'country': 'NO', 'elements': 'wind_from_direction'}


def get_data(endpoint, parameters):
    response = requests.get(endpoint, parameters, auth=(client_id, '')).json()
    json_data = response['data']
    return json_data


sources_data = get_data(sources_endpoint, sources_parameters)

list_date = []
for key in range(len(sources_data)):
    list_date.append(sources_data[key]["validFrom"])
list_date.sort()
list_oldest10 = list_date[0:10]

list_sources_id = []
for key in range(len(sources_data)):
    if sources_data[key]["validFrom"] in list_oldest10:
        list_sources_id.append(sources_data[key]["id"])

string_src_id = ','
observations_endpoint = 'https://frost.met.no/observations/v0.jsonld'
observations_parameters = {'sources': string_src_id.join(list_sources_id), 'elements': 'mean(wind_from_direction PT1H)',
                           'referencetime': '2010-04-01/2020-04-03'}

observations_data = get_data(observations_endpoint, observations_parameters)
print(observations_data)

