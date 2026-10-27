#!/usr/bin/env python3
"""Read a documented public USGS endpoint; no dependencies, account or API key."""
import json, urllib.request
URL = "https://waterservices.usgs.gov/nwis/iv/?format=json&sites=09380000,09402500&parameterCd=00060,00065"
with urllib.request.urlopen(URL, timeout=30) as response:
    print("HTTP", response.status)
    data = json.load(response)
for series in data["value"]["timeSeries"]:
    site = series["sourceInfo"]["siteCode"][0]["value"]
    variable = series["variable"]
    for block in series["values"]:
        methods = ", ".join(m.get("methodDescription", "") or str(m.get("methodID", "")) for m in block.get("method", []))
        for value in block["value"]:
            print(site, variable["variableCode"][0]["value"], methods, value["value"], variable["unit"]["unitCode"], value["dateTime"], value.get("qualifiers", []), sep=" | ")
