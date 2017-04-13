import json

from analytics.client import AnalyticsClient


with open ('../credentials.json') as json_data:
credentials = json.load(json_data)


client = AnalyticsClient(credentials['app_id'], credentials['api_key'])
query = "exceptions | where timestamp >="+
"datetime(2017-04-05T11:29:59.999Z) and timestamp <"+
"datetime(2017-04-06T11:30:00.001Z) | where"+
"customDimensions.['APIName'] == 'ABB' or customDimensions.['APIName']"+
"== 'GPM'  | project timestamp, customDimensions, outerMessage"
result = client.query(query)

json.loads(str(result[1][2]))['APIName']

json.loads(str(result[0][2]))['timestamp']

json.loads(result[0][1])[0]['message']


datetime.datetime.strptime((str(result[0][1]))[:19], "%Y-%m-%d %H:%M:%S")



def main():
    pass


def extractionAppInsight():
	with open ('../credentials.json') as json_data:
	credentials = json.load(json_data)
	client = AnalyticsClient(credentials['app_id'], credentials['api_key'])
	query = "exceptions | where timestamp >=" +
	"datetime(2017-04-05T11:29:59.999Z) and timestamp <" +
	"datetime(2017-04-06T11:30:00.001Z) | where"+
	"customDimensions.['APIName'] == 'ABB' or customDimensions.['APIName']"+
	"== 'GPM'  | project timestamp, customDimensions, outerMessage"

	result = client.query(query)


def createResponse():
pass


if __name__ == "__main__":
    main()
