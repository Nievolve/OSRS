# För eget bruk.
# Beräkna OSRS relaterade saker
# 
import XP
import items

# Programmet beräknar XP i game loop

# Variablar

def prayerXP():

    while True:
        print("Skriv antal bones")
        bones = int(input(": "))
        print("Skriv antal big bones")
        big_bones = int(input(": "))
        print("Skriv antal sun kissed bones")
        sun_kissed=int(input(": "))
        print("Skriv antal blessedboneshard")
        blessedBoneShard= int(input(": "))


        print(blessedBoneShard+XP.Total_Prayer_XP(bones*items.bones.blessedBoneShard)+XP.Total_Prayer_XP(big_bones*items.big_bones.blessedBoneShard+XP.Total_Prayer_XP(sun_kissed*items.sun_kissed_bones.blessedBoneShard)))
        break
def fletching():
    pass
# Mainloop
while True:
    print("Banked XP Calc")
    print("""
Choose.
          1. Calc prayer xp
          2. Calc fletching xp
""")
    menu = int(input("Choose"))
    if menu == 1:
        prayerXP()
    elif menu == 2:
        fletching()

    elif menu==0:
        break
