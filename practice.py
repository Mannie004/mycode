import requests

hockey = requests.get("http://statsapi.web.nhl.com/api/v1/teams").json()

print(hockey['teams'][0])


for x in (hockey['teams']):
        print(x)
        print(x['name'])
