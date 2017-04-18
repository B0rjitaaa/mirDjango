import json

from analytics.client import AnalyticsClient

from main.models import ExceptionMessage

import datetime


with open ('../credentials.json') as json_data:
	credentials = json.load(json_data)


client = AnalyticsClient(credentials['app_id'], credentials['api_key'])

query = "exceptions"\
"| where timestamp >= datetime(2017-04-13T11:29:59.999Z) and timestamp < datetime(2017-04-16T11:30:00.001Z)"\
"| where customDimensions.['APIName'] == 'ABB'"\
" or customDimensions.['APIName'] == 'GPM'"\
" or customDimensions.['APIName'] == 'Inaccess'"\
" or customDimensions.['APIName'] == 'Draker'"\
"| project timestamp, details, customDimensions"

result = client.query(query)

json.loads(str(result[1][2]))['APIName']

json.loads(str(result[0][2]))['timestamp']

datetime.datetime.strptime((str(result[0][1]))[:19], "%Y-%m-%d %H:%M:%S")

dict_size = len(result[0])

if dict_size > 0:
	for i in range(dict_size):
		date = datetime.datetime.strptime((str(result[0][i]))[:19], "%Y-%m-%d %H:%M:%S")
		api_name = json.loads(result[2][i])['APIName']
		detail = json.loads(result[1][i])[0]['message']
		exceptionMessage = ExceptionMessage(
				date=date,
				api_name=api_name,
				detail=detail
			)
		exceptionMessage.save()
