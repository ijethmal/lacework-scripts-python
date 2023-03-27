import requests
import json
import laceworktoken

#request to get ALL ALERTS no searching
account = "secureauth.lacework.net"
token_body = {
  "paging": {
    "rows": 1000,
    "totalRows": 3120,
    "urls": {
      "nextPage": "https://YourLacework.lacework.net/api/v2/Alerts/AbcdEfgh123..."
    }
  }
}
jsontoken_body = json.dumps(token_body)

#send request
r = requests.get("https://secureauth.lacework.net/api/v2/Alerts", headers={"Authorization": "Bearer {}".format(laceworktoken.token), "Content-Type": "application/json"}, json=jsontoken_body)

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
  

#print(response)


