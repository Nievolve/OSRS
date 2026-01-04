from enum import IntEnum

class bones:
    class bones:
        class prayer:
            bury                = 4
            blessedBoneShard    = 4
            crafting            = 5
        
    class big_bones:
        class prayer:
            bury                = 15
            blessedBoneShard    = 12
            crafting            = 5

    class baby_dragon_bones:
        class prayer:
            bury                = 0
            blessedBoneShard    = 24
            crafting            = 5 

    class dragon_bones:
        name                    = "dragon bones"
        class prayer:
            bury                = 0
            offer_wild          = 504
            blessedBoneShard    = 58
            crafting            = 5
    class sun_kissed_bones:
        class prayer:
            bury                = 0
            blessedBoneShard    = 45
            crafting            = 5

class log:
    class maple:
        class fletching:
            shortbow_xp         = 50
            shortbow_lvl        = 50
            longbow_xp          = 55
            longbow_lvl         = 55

            class vale_totem:
                totem_xp        = 50.8
                decoration_xp   = 201
    class yew:
        class fletching:
            shortbow_xp         = 67.5
            shortbow_lvl        = 65
            longbow_xp          = 75
            longbow_lvl         = 75
            class vale_totem:
                build_xp        = 82.6
                decoration_xp   = 326.2
                totem_xp        = build_xp * 4 + decoration_xp * 4 
    class magic:
        class fletching:
            shortbow_xp         =83.3
            class vale_totem:
                build_xp        =156.1
                decoration_xp   =619.8
                totem_xp        = build_xp* 4 + decoration_xp * 4
    # Index list for OSRS offical API            

class osrs_skill(IntEnum):
    OVERALL = 0
    ATTACK = 1
    DEFENCE = 2
    STRENGTH = 3
    HITPOINTS = 4
    RANGED = 5
    PRAYER = 6
    MAGIC = 7
    COOKING = 8
    WOODCUTTING = 9
    FLETCHING = 10
    FISHING = 11
    FIREMAKING = 12
    CRAFTING = 13
    SMITHING = 14
    MINING = 15
    HERBLORE = 16
    AGILITY = 17
    THIEVING = 18
    SLAYER = 19
    FARMING = 20
    RUNECRAFTING = 21
    HUNTER = 22
    CONSTRUCTION = 23

class skills_index(IntEnum):
    RANK = 0
    LEVEL = 1
    XP = 2



