import math
import items

def scale(in_value, inMin, inMax, outMin, outMax):
    return ((outMax-outMin) / (inMax-inMin))*(in_value - inMin) + outMin
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
            return l
        elif XP(l) > current_xp and mode == 2:
            diff_XP = current_xp-XP(l)
            scaled = scale(500, 0, 1000, 0, 100) # test
            print(l)
            print(scaled)
            return l+scaled
            
        else:
            print("Out of range")


def diff_XP(L1,L2):
    # Return differansen mellan L1-L2 i xp.
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
    if log == "maple":
        package = items.log.maple.fletching.vale_totem.totem_xp + (items.log.maple.fletching.vale_totem.decoration_xp*4) + (items.log.maple.fletching.longbow_xp*4)
    elif log == "yew":
        package = items.log.yew.fletching.vale_totem.totem_xp + (items.log.yew.fletching.vale_totem.decoration_xp*4) + (items.log.yew.fletching.shortbow_xp*4)
    
    work_xp = XP(target_lvl) - read_value
    print(f"Antal {log} logs som krävs : {math.ceil(work_xp/package*5)})")

#vale_totem("yew",65,69)
print(xp_to_lvl(300, 2))
#print(XP(99))
