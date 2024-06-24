# This code sample uses the 'requests' library:
# http://docs.python-requests.org

# Used package requests module are used to make api calls
import requests

# from "requests.auth" package use "HTTPBasicAuth" module
# basic httpbasicauthentication
from requests.auth import HTTPBasicAuth

# we are using json to load the json
import json

url = "https://name_of_the_project_jira.atlassian.net/rest/api/3/project"

auth = HTTPBasicAuth("email_id", "api_token")

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

# jira will give you all project details
# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

output = json.loads(response.text) # parse json information convert json to dictionary and execute operations on dictionaries

name = output[0]['name']
# first project name
print(name)
# you can use for loop to print list of projects