import requests
import json
import laceworktoken

account = "secureauth.lacework.net"

token_body = {
  "paging": {
    "rows": 1000,
    "totalRows": 3120,
    "urls": {
      "nextPage": "https://YourLacework.lacework.net/api/v2/Alerts/AbcdEfgh123..."
    }
  },
  "data": [
    {
      "startTime": "2023-03-18",
      "severity": "High",
      "endTime": "2023-03-20"
    }
  ]
}

jsontoken_body = json.dumps(token_body)
#print(jsontoken_body)

r = requests.get("https://secureauth.lacework.net/api/v2/Alerts", headers={"Authorization": "Bearer {}".format(laceworktoken.token), "Content-Type": "application/json"}, json=jsontoken_body)

print(r)

response = r.json()['data'][0]

print(response)