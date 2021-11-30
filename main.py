import zkb_import as zkb
from esi_import import esi_import
from loss_mail_export import loss_export
from inv_types import things_lost

if __name__ == "__main__":
    print("What would you like to do?")
    print("1 = Import new kills")
    print("2 = Grab Kill Info from ESI")
    print("3 = Output modules and ships lost")
    print("4 = Quit")

    u_start = int(input("What would you like to do: "))  # u_start = user_input

    while True:
        if u_start == 1:
            full_df = zkb.systemregions(zkb.systemsmap, zkb.regionsmap).set_index("solarSystemName")
            item_id = zkb.get_system_id(full_df)
            fetch_id = item_id[0]
            cos = item_id[1]
            zkb.killhash(fetch_id, cos)
        if u_start == 2:
            esi_import()
            loss_export()
        if u_start == 3:
            things_lost()
        if u_start == 4:
            break
        u_start = int(input("Anything Else?: "))
