#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python example script showing proper use of the Cisco Sample Code header.
Copyright (c) 2020 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""


__author__ = "Josh Ingeniero <jingenie@cisco.com>"
__copyright__ = "Copyright (c) 2020 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"



import requests
from app import app
import json
import pprint

pp = pprint.PrettyPrinter(indent=4)


def alert_handler(alert):
    remove = ('version', 'sharedSecret', 'sentAt')
    for item in remove:
        alert.pop(item, None)
    # AP went down
    if alert['alertType'] == "APs went down":
        payload = {
            "briefDescription": "{} AP went down".format(alert['deviceName']),
            "request": "Please check {}".format(json.dumps(alert['deviceUrl'], indent=4)),
            "action": "An AP went down. You may view the device on Meraki Dashboard using the URL provided. \
             Refer to the below alert message for more information.\n{}".format(json.dumps(alert, indent=4)),
            "callerLookup": {
              "id": app.config['TOPDESK_CALLER_ID']
            },
            "category": {
                "name": app.config['TOPDESK_AP_CATEGORY_NAME']
            },
            "subcategory": {
                "name": app.config['TOPDESK_AP_SUBCATEGORY_NAME']
            },
            "callType": {
                "name": app.config['TOPDEK_CALLTYPE_NAME']
            },
            "entryType": {
                "name": app.config['TOPDEK_ENTRYTYPE_NAME']
            }
        }
    # network usage
    elif alert['alertType'] == "Network usage alert":
        payload = {
            "briefDescription": "Network {} is over the usage threshold".format(alert['networkName']),
            "request": "Please check {}".format(json.dumps(alert['networkUrl'], indent=4)),
            "action": "A Network is over the usage threshold. You may view the network on Meraki Dashboard using the \
                      URL provided. Refer to the below alert message for more information.\n{} \
                      ".format(json.dumps(alert, indent=4)),
            "callerLookup": {
              "id": app.config['TOPDESK_CALLER_ID']
            },
            "category": {
                "name": app.config['TOPDESK_NETWORK_CATEGORY_NAME']
            },
            "subcategory": {
                "name": app.config['TOPDESK_NETWORK_SUBCATEGORY_NAME']
            },
            "callType": {
                "name": app.config['TOPDEK_CALLTYPE_NAME']
            },
            "entryType": {
                "name": app.config['TOPDEK_ENTRYTYPE_NAME']
            }
        }
    # settings changed
    elif alert['alertType'] == "Settings changed":
        payload = {
            "briefDescription": "Configuration change",
            "request": "Please check {}".format(json.dumps(alert['networkUrl'], indent=4)),
            "action": "A Configuration change has occurred. You may view the network on Meraki Dashboard using the \
                      URL provided. Refer to the below alert message for more information.\n{} \
                      ".format(json.dumps(alert, indent=4)),
            "callerLookup": {
              "id": app.config['TOPDESK_CALLER_ID']
            },
            "category": {
                "name": app.config['TOPDESK_SETTINGS_CATEGORY_NAME']
            },
            "subcategory": {
                "name": app.config['TOPDESK_SETTINGS_SUBCATEGORY_NAME']
            },
            "callType": {
                "name": app.config['TOPDEK_CALLTYPE_NAME']
            },
            "entryType": {
                "name": app.config['TOPDEK_ENTRYTYPE_NAME']
            }
        }
    # VPN Connectivity
    elif alert['alertType'] == "VPN connectivity changed":
        if alert['alertData']['connectivity'] == 'true':
            payload = 'NO ALERT'
        else:
            payload = {
                "briefDescription": "VPN connectivity down",
                "request": "Please check {}".format(json.dumps(alert['deviceUrl'], indent=4)),
                "action": "VPN Connectivity went down. You may view the network on Meraki Dashboard using the \
                      URL provided. Refer to the below alert message for more information.\n{} \
                      ".format(json.dumps(alert, indent=4)),
                "callerLookup": {
                  "id": app.config['TOPDESK_CALLER_ID']
                },
                "category": {
                    "name": app.config['TOPDESK_VPN_CATEGORY_NAME']
                },
                "subcategory": {
                    "name": app.config['TOPDESK_VPN_SUBCATEGORY_NAME']
                },
                "callType": {
                    "name": app.config['TOPDEK_CALLTYPE_NAME']
                },
                "entryType": {
                    "name": app.config['TOPDEK_ENTRYTYPE_NAME']
                }
            }
    # Generic Alert
    else:
        payload = {
            "briefDescription": "{}".format(json.dumps(alert['alertType'], indent=4)),
            "request": "Please check {}".format(json.dumps(alert['networkUrl'], indent=4)),
            "action": "{} alert has occurred. You may view the network on Meraki Dashboard using the \
                              URL provided. Refer to the below alert message for more information.\n{} \
                              ".format(json.dumps(alert['alertType'], indent=4), json.dumps(alert, indent=4)),
            "callerLookup": {
              "id": app.config['TOPDESK_CALLER_ID']
            },
            "category": {
                "name": app.config['TOPDESK_GENERAL_CATEGORY_NAME']
            },
            "callType": {
                "name": app.config['TOPDEK_CALLTYPE_NAME']
            },
            "entryType": {
                "name": app.config['TOPDEK_ENTRYTYPE_NAME']
            }
        }
    return payload


# create an incident on topdesk
def create_incident(url, username, password, alert):
    url = url

    payload = alert_handler(alert)

    if payload == 'NO ALERT':
        return 0

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, auth=(username, password), headers=headers,
                                data=json.dumps(payload, indent=4).replace('\\n', '<br>'))

    print(response)

    pp.pprint(json.loads(response.content))
