import math
import eNum
import calc
import items
import skilling
import API

def XP(L):
    # Funktion som tar in level och ger tillbaka kumulativ xp till den leveln
    xp=0
    for l in range(1,L):
        xp+= math.floor(l+300*2**(l/7))
    return math.floor(xp*0.25)

# Läser in xp total och skcikar tillbaka lvl
def xp_to_lvl(current_xp, mode):
    xp_list = []
    for l in range(1,100):        
        xp_list.append([l,XP(l)])
        if XP(l) > current_xp and mode == 1:
            return l-1
        elif XP(l) > current_xp and mode == 2:
            return round((l-1)+(calc.scale(current_xp, XP(l-1), XP(l),0,100)*0.01),2)
            

def diff_XP(L1,L2):
    # Return delta xp mellan L1-L2 i xp.
    # XP värde 
    if L1>L2:
        return L1-L2
    else:
        return L2-L1
    
def Total_Prayer_XP(a):
    # a = antal blessedbones
    return a*5 

    ## För att räkna ut antal logs som krävs mellan nuvarande xp till ett visst mål lvl. Genom Vale Totem minigame
def vale_totem(log, current, target_lvl):

    if current < 99:
        read_value = XP(current)
    else:
        read_value = current
    if log == items.log.maple.name:
        per_log = calc.totem(skilling.activity.vale_totem.maple.totem_xp, items.log.maple.fletching.longbow_xp)
    elif log == items.log.yew.name:
        per_log = calc.totem(skilling.activity.vale_totem.yew.totem_xp, items.log.yew.fletching.shortbow_xp)
    elif log == items.log.magic.name:
        per_log = calc.totem(skilling.activity.vale_totem.magic.build_xp, items.log.magic.fletching.shortbow_xp)
    work_xp = XP(target_lvl) - read_value
    print(f"Antal {log} logs som krävs : {math.ceil(work_xp/per_log)}")

def chaos_temple(bone,amount):
    # Return amount XP from amount bones input
    if bone == items.bones.big_bones.name:
        return items.bones.big_bones.prayer.offer_wild * amount
    
    if bone == items.bones.dragon_bones.name:
        return items.bones.dragon_bones.prayer.offer_wild * amount
    
    if bone == items.bones.bones.name:
        return items.bones.bones.prayer.offer_wild * amount

def main():
      
    vale_totem(items.log.yew.name, xp_to_lvl(API.get_user("Runehexen")[eNum.eSkills.FLETCHING][eNum.eSkillIndex.XP],eNum.eMode.LEVEL),69)
    #print(xp_to_lvl(1*10**6, 2))
    #print(XP(99))
    print(xp_to_lvl
            (API.get_user("Runehexen")[eNum.eSkills.PRAYER][eNum.eSkillIndex.XP]
            + 
            chaos_temple(items.bones.dragon_bones.name,200),eNum.eMode.XP)
            )

if __name__ == "__main__":  
    main()