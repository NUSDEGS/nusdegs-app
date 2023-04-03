from modsplan import ModsPlan
from semester import semester

def add_special_sem(plan:ModsPlan):
    semesters = plan.sems 
    plan.sems = []
    aca_year = 0
    for i in range(16):
        sem_num = (i+1) % 4
        if sem_num == 0:
            sem_num = 4
            aca_year += 1
        if sem_num <= 2:
            indx = sem_num+aca_year*2-1
            semesters[indx].seq_num = i+1
            plan.sems.append(semesters[indx])
        else:
            plan.sems.append(semester(i+1,6))

def intern6(plan:ModsPlan):
    # simply add CP3880 to yr4 sem1
    plan.sems[12].modules.append("CP3880")
    plan.sems[12].cur_mcs += 12

def intern3_1(plan:ModsPlan):
    # add CP3200 to yr3 special sem1
    plan.sems[10].modules.append("CP3200")
    plan.sems[10].cur_mcs += 6

def intern3_2(plan:ModsPlan):
    # add CP3200 to yr2 special sem1
    plan.sems[6].modules.append("CP3200")
    plan.sems[6].cur_mcs += 6
    # add CP3202 to yr3 special sem1
    plan.sems[10].modules.append("CP3202")
    plan.sems[10].cur_mcs += 6


def intern_fyp(plan:ModsPlan,isFyp:bool,is6MonthInternship:bool,
               is3Month1Internship:bool,is3Month2Internships:bool):
    if isFyp:
        # Fyp stands for final year project. 
        # So we simply add it to semester 7, regardless of max_mcs
        plan.sems[12].modules.append("CP4101")
        plan.sems[12].cur_mcs += 12
    if is6MonthInternship:
        intern6(plan)
    if is3Month1Internship:
        intern3_1(plan)
    if is3Month2Internships:
        intern3_2(plan)
