import requests
import json
import laceworktoken

account = "secureauth.lacework.net"

token_body = {
    "timeFilter": 
{
    "startTime": "2023-03-18",
    "endTime": "2023-03-20"
},
"returns": 
    [
        "string"
    ]
}

jsontoken_body = json.dumps(token_body)
#print(jsontoken_body)

r = requests.get("https://secureauth.lacework.net/api/v2/AuditLogs", headers={"Authorization": "Bearer {}".format(laceworktoken.token), "Content-Type": "application/json"}, json=jsontoken_body)

print(r)

response = r.json()['data'][0]

print(response)