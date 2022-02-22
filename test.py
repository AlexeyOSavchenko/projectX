import requests
import re
from datetime import datetime, timedelta
import json

client_id = '0feca865-844a-4260-939a-a725430e72cc'


def get_data(endpoint, parameters):
    response = requests.get(endpoint, parameters, auth=(client_id, '')).json()
    json_data = response['data']
    return json_data


""" Get Norwegian weather stations which measures wind from direction"""
sources_endpoint = 'https://frost.met.no/sources/v0.jsonld'
sources_parameters = {'ids': 'SN*', 'country': 'NO', 'elements': 'wind_from_direction', 'validtime': '1800-01-01/2020-01-01'}
sources_data = get_data(sources_endpoint, sources_parameters)
list_sources_id = []
for key in range(len(sources_data)):
    list_sources_id.append(sources_data[key]["id"])


""""Search oldest periods of observations with wind_from_direction measures
    SN can have another date period ValidFrom and ValidTo, but wind direction measurements have a different period (from 
    Available time series with key wind_from_direction)"""
available_time_series_url = 'https://frost.met.no/observations/availableTimeSeries/v0.jsonld'
available_time_series_parameters = {'elements': 'wind_from_direction'}
available_time_series_data = get_data(available_time_series_url, available_time_series_parameters)
available_time_series_list = []
for key in range(len(available_time_series_data)):
    available_time_series_list.append((available_time_series_data[key]["validFrom"], available_time_series_data[key]["sourceId"]))
available_time_series_list.sort()
oldest_norveg_sources_id_list = []
for i in range(len(available_time_series_list)):
    for j in range(len(list_sources_id)):
        matchSN = re.search(r'SN\d*', available_time_series_list[i][1])
        if matchSN.group(0) == list_sources_id[j] and len(oldest_norveg_sources_id_list) != 10:
            matchDate = re.search(r'\d{4}-\d{2}-\d{2}', available_time_series_list[i][0])
            oldest_norveg_sources_id_list.append((matchSN.group(0), matchDate.group(0)))


"""Get observations from oldest 10 Norwegian weather stations with wind_from_direction measures"""
observations_endpoint = 'https://frost.met.no/observations/v0.jsonld'
for key in range(len(oldest_norveg_sources_id_list)):
    date_from = datetime.strptime(oldest_norveg_sources_id_list[key][1], '%Y-%m-%d').date()
    date_to = date_from + timedelta(days=30)
    date_from_to_str = str(date_from) + '/' + str(date_to)
    observations_parameters = {'sources': oldest_norveg_sources_id_list[key][0], 'elements': 'wind_from_direction',
                               'referencetime': date_from_to_str}
    observations_data = get_data(observations_endpoint, observations_parameters)
