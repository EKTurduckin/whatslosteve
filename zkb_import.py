import json
import requests
import pandas as pd

systemsmap = pd.read_csv("mapSolarSystems.csv")
regionsmap = pd.read_csv("mapRegions.csv")


def killhash(fetchid, cos):
    # fetch ID is Solar System ID or Corporation ID.
    # Corp ID will just need to be an input.
    # Solar System ID can be found using get_system_id()
    fetchmod = ""
    if cos == 1:
        fetchmod = "solarSystemID"
    if cos == 2:
        fetchmod = "corporationID"

    systemkills = requests.get(f"https://zkillboard.com/api/losses/{fetchmod}/{fetchid}/").text
    systemkills_info = json.loads(systemkills)

    zkb_info = open("zkb_info.csv", "w")

    for kill in systemkills_info:
        kill_id = kill["killmail_id"]
        kill_hash = kill["zkb"]["hash"]
        zkb_info.write(f'{kill_id},{kill_hash}\n')

    zkb_info.close()


def get_system_id(fulldataframe):
    s = fulldataframe["solarSystemID"]
    print("Do you want to look up a System or a Corporation?")
    print("1 for System")
    print("2 for Corporation")
    cos = int(input())
    if cos == 2:
        return int(input("Provide Corp ID: "))
    try:
        user_system = input("What System: ")
        return s[user_system], cos
    except KeyError:
        print("Invalid System")
        user_system = input()
        return s[user_system], cos


def systemregions(sysmap, remap):
    sysmap = sysmap.merge(remap, left_on="regionID", right_on="regionID")
    return sysmap[["solarSystemID", "solarSystemName", "regionName", "regionID"]]


if __name__ == "__main__":
    fulldataframe = systemregions(systemsmap, regionsmap).set_index("solarSystemName")
    item_id = get_system_id(fulldataframe)

    fetchid = item_id[0]
    cos = item_id[1]

    killhash(fetchid, cos)
