import json


def loss_export():
    items_lost = open("items_lost.csv", "w")
    ships_lost = open("ships_lost.csv", "w")
    with open("lost_modules.json") as file:
        killmails = json.load(file)
        ships_lost.write("typeID\n")
        items_lost.write("typeID\n")
        for mail in killmails:
            if mail["victim"]["ship_type_id"] != 670:
                ships_lost.write(f'{mail["victim"]["ship_type_id"]}\n')
            item = mail["victim"]["items"]
            for i in item:
                # Flags are: 5 == Cargo, 11<>18 == Low, 19<>26 == Mid, 27<>35 == High, 93<>95 == Rigs
                # ship_type_id 670 == Capsule
                if i["flag"] != 5:
                    items_lost.write(f'{i["item_type_id"]}\n')

    items_lost.close()
    ships_lost.close()
