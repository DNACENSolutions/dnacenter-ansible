#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: site_create
short_description: Resource module for Site Create
description:
- Manage operation create of the resource Site Create.
- Creates site with area/building/floor with specified hierarchy.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  site:
    description: Site Create's site.
    suboptions:
      area:
        description: Site Create's area.
        suboptions:
          name:
            description: Name of the area (eg Area1).
            type: str
          parentName:
            description: Parent name of the area to be created.
            type: str
        type: dict
      building:
        description: Site Create's building.
        suboptions:
          address:
            description: Address of the building to be created.
            type: str
          latitude:
            description: Latitude coordinate of the building (eg 37.338).
            type: int
          longitude:
            description: Longitude coordinate of the building (eg -121.832).
            type: int
          name:
            description: Name of the building (eg building1).
            type: str
          parentName:
            description: Parent name of building to be created.
            type: str
        type: dict
      floor:
        description: Site Create's floor.
        suboptions:
          height:
            description: Height of the floor (eg 15).
            type: int
          length:
            description: Length of the floor (eg 100).
            type: int
          name:
            description: Name of the floor (eg floor-1).
            type: str
          parentName:
            description: Parent name of the floor to be created.
            type: str
          rfModel:
            description: Type of floor. Allowed values are 'Cubes And Walled Offices',
              'Drywall Office Only', 'Indoor High Ceiling', 'Outdoor Open Space'.
            type: str
          width:
            description: Width of the floor (eg 100).
            type: int
        type: dict
    type: dict
  type:
    description: Type of site to create (eg area, building, floor).
    type: str
requirements:
- dnacentersdk >= 2.4.4
- python >= 3.5
notes:
  - SDK Method used are
    sites.Sites.create_site
  - Paths used are post /dna/intent/api/v1/site
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.site_create:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    site:
      area:
        name: string
        parentName: string
      building:
        address: string
        latitude: 0
        longitude: 0
        name: string
        parentName: string
      floor:
        height: 0
        length: 0
        name: string
        parentName: string
        rfModel: string
        width: 0
    type: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionStatusUrl": "string",
      "message": "string"
    }
"""
