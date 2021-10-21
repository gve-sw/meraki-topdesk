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



import os
import DETAILS
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    MERAKI_API_KEY = DETAILS.MERAKI_API_KEY
    MERAKI_ORGANIZATION_ID = DETAILS.MERAKI_ORGANIZATION_ID

    TOPDESK_USERNAME = DETAILS.TOPDESK_USERNAME
    TOPDESK_PASSWORD = DETAILS.TOPDESK_PASSWORD
    TOPDESK_URL = DETAILS.TOPDESK_URL

    TOPDESK_CALLER_ID = DETAILS.TOPDESK_CALLER_ID
    TOPDEK_CALLTYPE_NAME = DETAILS.TOPDEK_CALLTYPE_NAME
    TOPDEK_ENTRYTYPE_NAME = DETAILS.TOPDEK_ENTRYTYPE_NAME

    TOPDESK_AP_CATEGORY_NAME = DETAILS.TOPDESK_AP_CATEGORY_NAME
    TOPDESK_AP_SUBCATEGORY_NAME = DETAILS.TOPDESK_AP_SUBCATEGORY_NAME
    TOPDESK_NETWORK_CATEGORY_NAME = DETAILS.TOPDESK_NETWORK_CATEGORY_NAME
    TOPDESK_NETWORK_SUBCATEGORY_NAME = DETAILS.TOPDESK_NETWORK_SUBCATEGORY_NAME
    TOPDESK_SETTINGS_CATEGORY_NAME = DETAILS.TOPDESK_SETTINGS_CATEGORY_NAME
    TOPDESK_SETTINGS_SUBCATEGORY_NAME = DETAILS.TOPDESK_SETTINGS_SUBCATEGORY_NAME
    TOPDESK_VPN_CATEGORY_NAME = DETAILS.TOPDESK_VPN_CATEGORY_NAME
    TOPDESK_VPN_SUBCATEGORY_NAME = DETAILS.TOPDESK_VPN_SUBCATEGORY_NAME
    TOPDESK_GENERAL_CATEGORY_NAME = DETAILS.TOPDESK_GENERAL_CATEGORY_NAME
    TOPDESK_GENERAL_SUBCATEGORY_NAME = DETAILS.TOPDESK_GENERAL_SUBCATEGORY_NAME
