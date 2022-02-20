import requests
import json

client_id = '0feca865-844a-4260-939a-a725430e72cc'

sources_endpoint = 'https://frost.met.no/sources/v0.jsonld'
sources_parameters = {'ids': 'SN*', 'country': 'NO', 'elements': 'wind_from_direction', 'validtime': '1800-01-01/2000-01-01'}

def get_data(endpoint, parameters):
    response = requests.get(endpoint, parameters, auth=(client_id, '')).json()
    json_data = response['data']
    return json_data

sources_data = get_data(sources_endpoint, sources_parameters)

list_sources_id = []
for key in range(len(sources_data)):
    list_sources_id.append(sources_data[key]["id"])
print(list_sources_id)

""""Search oldest periods of observations with wind_from_direction measures"""
available_time_series_url = 'https://frost.met.no/observations/availableTimeSeries/v0.jsonld'
available_time_series_parameters = {'elements': 'wind_from_direction'}
available_time_series_data = get_data(available_time_series_url, available_time_series_parameters)
available_time_series_list = []
for key in range(len(available_time_series_data)):
    available_time_series_list.append((available_time_series_data[key]["validFrom"], available_time_series_data[key]["sourceId"]))
available_time_series_list.sort()
#print(available_time_series_list[0][1])
print(available_time_series_list)


oldest_norveg_sources_id = []
not_norveg = []
for i in range(len(available_time_series_list)):
    for j in range(len(list_sources_id)):
       if (available_time_series_list[i][1])[0:7] == list_sources_id[j] and len(oldest_norveg_sources_id) != 10:
            oldest_norveg_sources_id.append((available_time_series_list[i][1])[0:7])
print(oldest_norveg_sources_id)







# tmp_dict = {}
# for key in range(len(available_time_series_data)):
#     tmp_dict[available_time_series_data[key]] = available_time_series_data[key]["sourceId"]
# sorted_tuple = sorted(tmp_dict.items(), key=lambda x: x[0])
# print(sorted_tuple[0][1])

# string_src_id = ','
# tmp_list_src_id = []
# i = 0
# for j in range(len(list_sources_id)):
#     tmp_list_src_id.append(list_sources_id[j])
#     i += 1
#     if i == 255:
#         print(string_src_id.join(tmp_list_src_id))
#         tmp_list_src_id = []
#         i = 0

# string_src_id = ','
# available_time_series_url = 'https://frost.met.no/observations/availableTimeSeries/v0.jsonld'
# available_time_series_parameters = {'ids': string_src_id.join(list_sources_id), 'elements': 'wind_from_direction'}
# available_time_series_data = get_data(available_time_series_url, available_time_series_parameters)
# print(available_time_series_data)



# sources_data = get_data(sources_endpoint, sources_parameters)
#
# list_date = []
# for key in range(len(sources_data)):
#     list_date.append(sources_data[key]["validFrom"])
# list_date.sort()
# list_oldest10 = list_date[0:10]
# print(list_oldest10)
#
#
# list_sources_id = []
# for key in range(len(sources_data)):
#     if sources_data[key]["validFrom"] in list_oldest10:
#         list_sources_id.append(sources_data[key]["id"])
#
# string_src_id = ','
# print(string_src_id.join(list_sources_id))
# observations_endpoint = 'https://frost.met.no/observations/v0.jsonld'
# observations_parameters = {'sources': 'SN40250', 'elements': 'mean(wind_from_direction PT1H)',
#                            'referencetime': '2010-04-01/2020-04-03'}
#
# # observations_data = get_data(observations_endpoint, observations_parameters)
# response = requests.get(observations_endpoint, observations_parameters, auth=(client_id, '')).json()
# print(response)
#

# with open('data.txt', 'w') as f:
#     json.dump(observations_data, f)