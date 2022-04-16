import json
from urllib.request import urlopen

production_url='http://10.12.13.164:8110/api/BasicQMSData/BirichinaDataForReport?StartDate=2022-04-03&EndDate=2022-04-03'
response = urlopen(production_url)
production_data_json = json.loads(response.read())

print (production_data_json)