# Use offical OSRS API to get skills level/xp   

import requests



def get_user(username):
    empty_list = []
    filled_list = []
    url = "https://secure.runescape.com/m=hiscore_oldschool_ironman/index_lite.ws"
    rows = [
            line.split(",") for line in 
            requests.get(
                url, params={"player": username}).text.splitlines()
                ]
    # Exempel: Attack (index 1)
    for rank_lvl_xp in range(25):
        
        empty_list.append(rows[rank_lvl_xp])

    for skill in range(25):
        filled_list.append([
            int(empty_list[skill][0]),
            int(empty_list[skill][1]),
            int(empty_list[skill][2]),
        ])
    return filled_list
def main():
    print(get_user("Runehexen"))
    
    

if __name__ == "__main__":
    main()