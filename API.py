# Use offical OSRS API to get skills/level

import requests
def get_user(username):
    url = "https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws"

    response = requests.get(url, params={"player": username})
    response.raise_for_status()

    lines = response.text.splitlines()
    rows = [line.split(",") for line in lines]
    print(lines)
    # Exempel: Attack (index 1)
    attackRank, attackLevel, attackXp = rows[1]
    print(f"Attack: level {attackLevel}, xp {attackXp}")
    for k in range(0,24):
        rank, lvl, xp = rows[k]
        print(f"{k},  : {rank} | {lvl}  | {xp}")

def main():
    get_user("Runehexen")

if __name__ == "__main__":
    main()