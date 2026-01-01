# Use offical OSRS API to get skills/level

import requests

username = "Runehexen"
url = "https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws"

response = requests.get(url, params={"player": username})
response.raise_for_status()

lines = response.text.splitlines()
rows = [line.split(",") for line in lines]

# Exempel: Attack (index 1)
attackRank, attackLevel, attackXp = rows[1]
print(f"Attack: level {attackLevel}, xp {attackXp}")

# Exempel: Zulrah KC (index ~56, kan variera)
zulrahIndex = 56
zulrahRank, zulrahKC = rows[zulrahIndex]
print(f"Zulrah KC: {zulrahKC}")
