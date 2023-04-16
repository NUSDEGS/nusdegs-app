from ..modsplan import ModsPlan

def newQET(plan:ModsPlan,doesNeedQet:bool):
    if doesNeedQet:
        QET(plan,True)
    return

def QET(plan:ModsPlan,class1:bool):
    if class1:
        plan.sems[0].modules.append("ES1000")
        plan.sems[0].cur_mcs += 0
        plan.sems[1].modules.append("ES1103")
        plan.sems[1].cur_mcs += 4
    return
