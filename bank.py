# När man ska autoköra

import bones_types as b
import XP 

# Skills
prayerLVL=49


def bank():
    antal_big_bones = 211
    antal_bones = 271
    antal_sun_kissed = 34
    antal_blessed_boneshard = 6112

    total =6*  (antal_blessed_boneshard + (antal_big_bones*b.dragon_bones.blessedBoneShard) + (antal_bones* b.bones.blessedBoneShard)+ (antal_sun_kissed*b.sun_kissed_bones.blessedBoneShard))

    print(total)


