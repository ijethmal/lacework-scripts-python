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
  },
  "filters": [ #will only return medium severity alerts from specified machine
  #  { "field": "machineTags.AmiId", "expression": "eq", "value": "ami here" 
  #  },
    {
      "field": "severity", "expression": "eq", "value": "Medium"
    }
  ],
  "returns": [ 
    "severity", "status", "vulnId" 
    ]
}
jsontoken_body = json.dumps(token_body)
print(jsontoken_body)

#send request
hostvulnsurl = os.getenv('hostvulnsurl')
r = requests.post(hostvulnsurl, headers={"Authorization": "Bearer {}".format(laceworktoken.token), "Content-Type": "application/json"}, data=jsontoken_body)

#print status code (200/4XX/5XX)
print(r)

#overwrite existing alertsfile
with open("host vulns.txt", "w") as output_file:
    output_file.close()

#print output to console and alerts file
for i in range(len(r.json()['data'])):
  response = r.json()['data'][i]
  print(response)
  with open("host vulns.txt", "a") as output_file:
    print(response, file=output_file)
    output_file.close()
  

