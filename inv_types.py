import pandas as pd


def things_lost():
    with open("items_lost.csv", newline="", encoding="utf-8") as items:
        with open("ships_lost.csv", newline="", encoding="utf-8") as ships:
            with open("invTypes.csv", newline="", encoding="utf-8") as types:
                invTypes = pd.read_csv(types)
                ships_lost = pd.read_csv(ships)
                items_lost = pd.read_csv(items)

                items_lost = items_lost.merge(invTypes, left_on="typeID", right_on="typeID")
                ships_lost = ships_lost.merge(invTypes, left_on="typeID", right_on="typeID")

                items_lost = items_lost[["typeID", "typeName"]].groupby("typeName").count()
                ships_lost = ships_lost[["typeID", "typeName"]].groupby("typeName").count()

                print(items_lost.sort_values("typeID", ascending=False))
                print(ships_lost.sort_values("typeID", ascending=False))