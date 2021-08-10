#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: discovery_range_info
short_description: Information module for Discovery Range
description:
- Get all Discovery Range.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  startIndex:
    description:
    - StartIndex path parameter. Start index.
    type: int
  recordsToReturn:
    description:
    - RecordsToReturn path parameter. Number of records to return.
    type: int
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Discovery Range reference
  description: Complete reference of the Discovery Range object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Discovery Range
  cisco.dnac.discovery_range_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    startIndex: 0
    recordsToReturn: 0
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "attributeInfo": {},
          "cdpLevel": 0,
          "deviceIds": "string",
          "discoveryCondition": "string",
          "discoveryStatus": "string",
          "discoveryType": "string",
          "enablePasswordList": "string",
          "globalCredentialIdList": [
            "string"
          ],
          "httpReadCredential": {
            "comments": "string",
            "credentialType": "string",
            "description": "string",
            "id": "string",
            "instanceTenantId": "string",
            "instanceUuid": "string",
            "password": "string",
            "port": 0,
            "secure": true,
            "username": "string"
          },
          "httpWriteCredential": {
            "comments": "string",
            "credentialType": "string",
            "description": "string",
            "id": "string",
            "instanceTenantId": "string",
            "instanceUuid": "string",
            "password": "string",
            "port": 0,
            "secure": true,
            "username": "string"
          },
          "id": "string",
          "ipAddressList": "string",
          "ipFilterList": "string",
          "isAutoCdp": true,
          "lldpLevel": 0,
          "name": "string",
          "netconfPort": "string",
          "numDevices": 0,
          "parentDiscoveryId": "string",
          "passwordList": "string",
          "preferredMgmtIPMethod": "string",
          "protocolOrder": "string",
          "retryCount": 0,
          "snmpAuthPassphrase": "string",
          "snmpAuthProtocol": "string",
          "snmpMode": "string",
          "snmpPrivPassphrase": "string",
          "snmpPrivProtocol": "string",
          "snmpRoCommunity": "string",
          "snmpRoCommunityDesc": "string",
          "snmpRwCommunity": "string",
          "snmpRwCommunityDesc": "string",
          "snmpUserName": "string",
          "timeOut": 0,
          "updateMgmtIp": true,
          "userNameList": "string"
        }
      ],
      "version": "string"
    }
"""