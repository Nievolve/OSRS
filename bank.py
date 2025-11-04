# När man ska autoköra

import bones_types as b
import XP 

# Testing
antal_big_bones = 211
antal_bones = 271
antal_sun_kissed = 34
antal_blessed_boneshard = 6112 + (antal_big_bones*b.dragon_bones.blessedBoneShard) + (antal_bones* b.bones.blessedBoneShard)+ (antal_sun_kissed*b.sun_kissed_bones.blessedBoneShard)
total = antal_blessed_boneshard*6

print(total)


