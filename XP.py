import math
import items

def scale(in_value, inMin, inMax, outMin, outMax):
    return (in_value - inMin) / (inMax - inMin) * (outMax - outMin)
def XP(L):
    # Funktion som tar in level och ger tillbaka kumulativ xp till den leveln
    xp=0
    for l in range(1,L):
        xp+= math.floor(l+300*2**(l/7))
    return math.floor(xp*0.25)

# Läser in xp total och skcikar tillbaka lvl
def xp_to_lvl(current_xp, mode):
    if mode == 1:
        xp_list = []
        xp=0
        for l in range(1,100):        
            xp_list.append([l,XP(l)])
            if XP(l) > current_xp:
                return l
    elif mode == 2:
        pass
    else:
        print("Out of range")

def from_current_lvl(current_lvl, target_lvl):
    target_xp = XP(target_lvl)
    try_lvl= 1
    while True:
        print(XP(try_lvl))
        if XP(try_lvl) >= target_xp:
            break
        else:
            try_lvl += try_lvl
    print("found lvl" ,try_lvl)
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
print(xp_to_lvl(300))
#print(XP(99))
