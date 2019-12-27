#!/usr/bin/env python3
import pprint
import requests
import json
import polling
import pytest

personal_access_token = 'xxx'
organization_url = "https://dev.azure.com/ketansony/6d52d6ae-d077-44f3-8024-97cadee02e1b"
headers = {
	    'authorization': "Basic xxx",
	    'content-type': "application/json"
	    }

def trigger_pipeline():
	trigger_pipeline_querystring = {"ignoreWarnings":"false","api-version":"5.0"}
	trigger_pipeline_payload = "{\"definition\":{\"id\":1}}"
	trigger_pipeline_response = requests.request("POST", organization_url+"/_apis/build/builds", 
		data=trigger_pipeline_payload, headers=headers, params=trigger_pipeline_querystring)
	return json.loads(trigger_pipeline_response.text).get('id')

def is_correct_response(response):
	    return response == 'completed'

def wait_for_pipeline_status_to_be_completed(build_id):
	pipeline_status_url = organization_url+"/_apis/build/Builds/"+str(build_id)
	
	polling.poll(
	    lambda: json.loads(requests.request("GET", pipeline_status_url, headers=headers).text).get('status'),
	    check_success=is_correct_response,
	    step=1,
	    timeout=60)

def get_pipeline_result(build_id):
	return requests.request("GET", organization_url+"/_apis/build/Builds/"+str(build_id), headers=headers)

def test_pipeline():
	build_id = trigger_pipeline()
	wait_for_pipeline_status_to_be_completed(build_id)
	pipeline_result_response = get_pipeline_result(build_id)
	assert json.loads(pipeline_result_response.text).get('result') == "succeeded"

			



