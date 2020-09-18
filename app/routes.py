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


from flask import render_template, flash, redirect, url_for, request
from app import app
import logging
import pprint
import meraki as mk
import TopDeskHelper


pp = pprint.PrettyPrinter(indent=4)
org_id = app.config['MERAKI_ORGANIZATION_ID']
user = app.config['TOPDESK_USERNAME']
password = app.config['TOPDESK_PASSWORD']
url = app.config['TOPDESK_URL']
dashboard = mk.DashboardAPI(app.config['MERAKI_API_KEY'])

logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


# webhook handler
@app.route('/', methods=['POST'])
def alert():
    if not request.json:
        return ("invalid data", 400)
    logging.warning(request.json)
    print(request.json["alertType"])
    TopDeskHelper.create_incident(url, user, password, request.json)
    return "Success"


# uplink status
@app.route('/stats', methods=['GET'])
def stats():
    statistics = dashboard.organizations.getOrganizationDevicesUplinksLossAndLatency(org_id)
    return render_template('index.html', title='Home', statistics=statistics)
