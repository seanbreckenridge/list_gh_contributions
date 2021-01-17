import sys
import csv
import json
from . import JsonList


def json_printer(data: JsonList) -> None:
    print(json.dumps(data))


def csv_printer(data: JsonList) -> None:
    csv_rows = []
    csv_rows.append(["name", "url", "license", "updatedAt"])
    for repo in data:
        license = ""
        if "licenseInfo" in repo and repo["licenseInfo"] is not None:
            license = repo["licenseInfo"]["name"]
        csv_rows.append([repo["name"], repo["url"], license, repo["updatedAt"]])
    writer = csv.writer(sys.stdout, delimiter=",", quoting=csv.QUOTE_ALL)
    writer.writerows(csv_rows)
