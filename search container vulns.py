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
    "startTime": "2023-03-20T08:00:00.000Z",
    "endTime": "2023-03-26T08:00:00.000Z"
  }
  #"filters": [ 
  #  { "field": "vulnId", "expression": "eq", "value": "insert vulnId here" },
  #  } 
  #]
}
jsontoken_body = json.dumps(token_body)
print(jsontoken_body)

#send request
containervulnsurl = os.getenv('containervulnsurl')
r = requests.post(containervulnsurl, headers={"Authorization": "Bearer {}".format(laceworktoken.token), "Content-Type": "application/json"}, data=jsontoken_body)

#print status code (200/4XX/5XX)
print(r)

#overwrite existing alertsfile
with open("container vulns.txt", "w") as output_file:
    output_file.close()

#print output to console and alerts file
for i in range(len(r.json()['data'])):
  response = r.json()['data'][i]
  print(response)
  with open("container vulns.txt", "a") as output_file:
    print(response, file=output_file)
    output_file.close()
  

