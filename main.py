# För eget bruk.
# Beräkna OSRS relaterade saker
# 
import XP
import bones_types
import bank
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


        print(blessedBoneShard+XP.Total_Prayer_XP(bones*bones_types.bones.blessedBoneShard)+XP.Total_Prayer_XP(big_bones*bones_types.big_bones.blessedBoneShard+XP.Total_Prayer_XP(sun_kissed*bones_types.sun_kissed_bones.blessedBoneShard)))
        break

# Mainloop
while True:
    print("Banked XP Calc")
    print("""
Choose.
          1. Calc prayer xp
""")
    menu = int(input("Choose"))
    if menu==1:
        prayerXP()
    elif menu==9:
        bank.bank()

    elif menu==0:

        break
