# add UE modules
from module import module
from semester import semester
from modsplan import ModsPlan
import math

def add_UE(plan):
    # calculate num of UE to add
    plan_mcs = plan.get_cur_mcs()
    add_ue = math.ceil((160-plan_mcs)/4)
    # add UE mods to plan
    for i in range(16):
        if i % 4 == 0 or i % 4 == 1:
            count = 0
            while plan.sems[i].if_under_maxmcs():
                plan.add_module(i,'UE')
                add_ue -= 1
                count += 1
                # at most 3 UE in each sem
                if count==3:
                    break
                if add_ue == 0:
                    break
        if add_ue == 0 :
            break
    
            