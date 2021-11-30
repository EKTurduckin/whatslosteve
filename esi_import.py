import json
import requests
import csv


def esi_import():
    with open("zkb_info.csv", newline="") as csvfile:
        zkb_info = csv.reader(csvfile, delimiter=",")
        lost_modules = open("lost_modules.json", "w")
        eachkill = []
        remaining = 200
        for row in zkb_info:
            esikill = requests.get(f"https://esi.evetech.net/latest/killmails/{row[0]}/{row[1]}/?datasource=tranquility").text
            kill_info = json.loads(esikill)
            eachkill.append(kill_info)
            remaining -= 1
            print(remaining)

        json.dump(eachkill, lost_modules)
        lost_modules.close()
