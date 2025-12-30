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

def nuvarande_xp(current_xp, target_lvl):
    curr_xp = current_xp 
    work = False
    xp_check    = 0
    loop        = 1
    found_level = 1
    while not work:
        xp_check+=math.floor(loop+300*2**(loop/7))
        print("xp_check", xp_check)
        print("curr_xp", curr_xp)
        if xp_check >= curr_xp:
            work = True
            print("My found lvl" ,found_level)
        else:
            loop += loop
            found_level += found_level
    my_xp = XP(found_level)
    leftover = current_xp - my_xp
    amount_level_xp = diff_XP(my_xp,target_lvl)
    procent = scale(leftover,XP(target_lvl)-amount_level_xp,amount_level_xp,0,100)
    print("My leftover", leftover)
    print("My lvl" ,my_xp)
    print("My procent" ,procent)

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
    print(package)
    print(work_xp)
    print(math.ceil(work_xp/package*5,))

vale_totem("maple",48,65)