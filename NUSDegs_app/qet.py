from modsplan import ModsPlan
from semester import semester


def newQET(plan:ModsPlan,doesNeedQet:bool):
    if doesNeedQet:
        QET(plan,True)

def QET(plan:ModsPlan,class1:bool):
    start_sem = 0
    mod_mcs = 4
    if class1:
        plan.sems[0].modules.append("ES1000")
        start_sem = 1
    for i in range(start_sem,16):
        if i % 4 == 3:
            # not provided in special term II
            continue
        if plan.sems[i].cur_mcs+mod_mcs<=plan.sems[i].max_mcs:
            plan.sems[i].modules.append("ES1103")
            plan.sems[i].cur_mcs += mod_mcs
            return

