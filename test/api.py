import pprint
import requests
import json

r = requests.get('https://dev.azure.com/ketansony/6d52d6ae-d077-44f3-8024-97cadee02e1b/_apis/build/Builds/13', auth=('ketansony', personal_access_token))
print(json.loads(r.text).get('result'))
