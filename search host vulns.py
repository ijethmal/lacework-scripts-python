import requests
import json
import laceworktoken

#request to SEARCH FOR SPECIFIC ALERTS
account = "secureauth.lacework.net"
token_body = {
  "timeFilter": {
    "startTime": "2023-03-20T08:00:00.000Z",
    "endTime": "2023-03-26T08:00:00.000Z"
  },
  "filters": [ #will only return medium severity alerts from pen test server ip-10-255-255-6.ec2.internal
    { "field": "machineTags.AmiId", "expression": "eq", "value": "ami-09a41e26df464c548" 
    },
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
#note!! for post requests, it's data not json
r = requests.post("https://secureauth.lacework.net/api/v2/Vulnerabilities/Hosts/search", headers={"Authorization": "Bearer {}".format(laceworktoken.token), "Content-Type": "application/json"}, data=jsontoken_body)

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
  

