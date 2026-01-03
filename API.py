# Use offical OSRS API to get skills level/xp   

import requests

import items


def get_user(username):
    empty_list = []
    filled_list = []
    url = "https://secure.runescape.com/m=hiscore_oldschool_ironman/index_lite.ws"
    response = requests.get(url, params={"player": username})
    response.raise_for_status()

    lines = response.text.splitlines()
    rows = [line.split(",") for line in lines]
    # Exempel: Attack (index 1)
    for k in range(24):
        
        empty_list.append(rows[k])
    #    print(f"{k},  : {items.osrs_skill_list[k]} | {empty_list[k][1]} | {empty_list[k][2]}")
    for j in range(24):
        filled_list.append([
            int(empty_list[j][0]),
            int(empty_list[j][1]),
            int(empty_list[j][2]),
        ])
    return filled_list
def main():
    get_user("Runehexen")

if __name__ == "__main__":
    main()