import requests
from requests.auth import HTTPBasicAuth
import json

# flask is a package
# Flask is a module
from flask import Flask, request,jsonify

# create an object to Flask
# using this instance we will perform all actions
app = Flask(__name__)

# @app is decorator
# decorator execute route function before fun() function
# why decprator?
# example: 
# allowing authenticated users should access particular microservice(payments)
# or
# before createJira() function execution run only authenticated users
@app.route("/createJira", methods=['POST'])
def createJira():
    url = "https://name_of_the_project_jira.atlassian.net/rest/api/3/project"

    auth = HTTPBasicAuth("email_id", "api_token")

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps( {
        "fields": {
        "description": {
            "content": [
                {
                    "content": [
                        {
                            "text": "12:40 jira ticket",
                            "type": "text"
                        }
                    ],
                    "type": "paragraph"
                    }
                ],
            "type": "doc",
            "version": 1
        },
        # https://name_of_the_project.atlassian.net/jira/software/projects/SCRUM/settings/issuetypes/10003
        # Projects => name_of_the_project => Project settings => Issue types
        "issuetype": {
            "id": "10003"
        },
        "project": {
            "key": "SCRUM"
        },
        "summary": "12:40pm jira ticket",
        },
        "update": {}
    } )

    # Ensure the request is JSON
    if request.is_json:
        event_data = request.json

        # Extract information from the webhook payload
        if 'issue' in event_data and 'comment' in event_data:
            issue_title = event_data['issue']['title']
            comment_body = event_data['comment']['body']

            # Check if the comment contains the /jira command
            if comment_body.startswith('/jira'):
                response = requests.request(
                    "POST",
                    url,
                    data=payload,
                    headers=headers,
                    auth=auth
                )
            else:
                return jsonify({"error": "Comment does not contain the /jira command"}), 400
        else:
            return jsonify({"error": "Invalid event data"}), 400
    else:
        return jsonify({"error": "Request content-type must be application/json"}), 400

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

# create an api and deploy an api
# Flask has inbuilt server to execute the python program
# no need of tomcat or nginix server
# default flask port : 5000
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)

# Locally we cannot run this script because in github webhook needs an public ipv4 address that can be accessible