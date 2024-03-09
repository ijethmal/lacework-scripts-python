import requests
import json
import laceworktoken
import os 
import dotenv
from dotenv import load_dotenv

#request to SEARCH FOR SPECIFIC ALERTS
load_dotenv()
account = os.getenv('account')
account = account
token_body = {
  "timeFilter": {
    "startTime": "2023-03-25T08:00:00.000Z",
    "endTime": "2023-03-26T08:00:00.000Z"
  },
  "filters": [
    {
      "field": "severity",
      "expression": "eq",
      "value": "High"
    }
  ],
  "returns": [
    "alertId", "startTime", "alertName", "alertType", "alertInfo"
  ]
}
jsontoken_body = json.dumps(token_body)
print(jsontoken_body)

#send request
#note!! for post requests, it's data not json
alertsurl = os.getenv('alertsurl')
r = requests.post(alertsurl, headers={"Authorization": "Bearer {}".format(laceworktoken.token), "Content-Type": "application/json"}, data=jsontoken_body)

#print status code (200/4XX/5XX)
print(r)

#overwrite existing alertsfile
with open("alerts.txt", "w") as output_file:
    output_file.close()

#print output to console and alerts file
for i in range(len(r.json()['data'])):
  response = r.json()['data'][i]
  print(response)
  with open("alerts.txt", "a") as output_file:
    print(response, file=output_file)
    output_file.close()
  

