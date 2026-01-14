from enum import IntEnum

class eSkills(IntEnum):
    OVERALL         = 0
    ATTACK          = 1
    DEFENCE         = 2
    STRENGTH        = 3
    HITPOINTS       = 4
    RANGED          = 5
    PRAYER          = 6
    MAGIC           = 7
    COOKING         = 8
    WOODCUTTING     = 9
    FLETCHING       = 10
    FISHING         = 11
    FIREMAKING      = 12
    CRAFTING        = 13
    SMITHING        = 14
    MINING          = 15
    HERBLORE        = 16
    AGILITY         = 17
    THIEVING        = 18
    SLAYER          = 19
    FARMING         = 20
    RUNECRAFTING    = 21
    HUNTER          = 22
    CONSTRUCTION    = 23
    SAILING         = 24

class eSkillIndex(IntEnum):
    RANK = 0
    LEVEL = 1
    XP = 2

class eMode(IntEnum):
    LEVEL           =1
    XP              =2
