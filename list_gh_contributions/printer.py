import sys
import csv
import json
from . import JsonList


def json_printer(data: JsonList) -> None:
    print(json.dumps(data))


def csv_printer(data: JsonList) -> None:
    csv_rows = []
    csv_rows.append(["name", "updatedAt", "url"])
    for repo in data:
        csv_rows.append([repo["name"], repo["updatedAt"], repo["url"]])
    writer = csv.writer(sys.stdout, delimiter=",", quoting=csv.QUOTE_ALL)
    writer.writerows(csv_rows)
