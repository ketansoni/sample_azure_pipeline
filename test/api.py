import pprint
import requests
import json


#Trigger Build Pipeline
organization_url = "https://dev.azure.com/ketansony/6d52d6ae-d077-44f3-8024-97cadee02e1b"
trigger_pipeline_querystring = {"ignoreWarnings":"false","api-version":"5.0"}
trigger_pipeline_payload = "{\"definition\":{\"id\":1}}"
headers = {
    'content-type': "application/json"
    }

trigger_pipeline_response = requests.request("POST", organization_url+"/_apis/build/builds", data=trigger_pipeline_payload, headers=headers, params=trigger_pipeline_querystring)
build_id = json.loads(trigger_pipeline_response.text).get('id')
print(build_id)

#Get Build Run Result
pipeline_result_response = requests.request("GET", organization_url+"/_apis/build/Builds/"+str(build_id), headers=headers)
print(json.loads(pipeline_result_response.text).get('status'))
