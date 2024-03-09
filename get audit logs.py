import requests
import json
import laceworktoken
import os 
import dotenv
from dotenv import load_dotenv

load_dotenv()
account = os.getenv('account')
account = account

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
logsurl = os.getenv('auditlogsurl')
r = requests.get(logsurl, headers={"Authorization": "Bearer {}".format(laceworktoken.token), "Content-Type": "application/json"}, json=jsontoken_body)

print(r)

#overwrite existing alertsfile
with open("auditlogs.txt", "w") as output_file:
    output_file.close()

for i in range(len(r.json()['data'])):
  response = r.json()['data'][i]
  print(response)
  with open("auditlogs.txt", "a") as output_file:
    print(response, file=output_file)
    output_file.close()

print(response)