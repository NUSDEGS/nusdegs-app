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
            plan.sems.append(semester(i+1,20)) # consider max_mc

def intern6(plan:ModsPlan):
    # There are 3 courses representing 6 month internship:
    # CP3880, IS4010 and TR3202
    # CP3880 is the most general option to choose.
    # All the prerequistes of CP3880 are fulfilled by basic degree requirements
    # IS4010 has two parts. 
    # It will start a 3-month full-time internship in special semester,
    # and continue with a part-time internship in the following semester
    #  (semester 1 in next academic year)
    # IS4010 also requires IS3103 (extra), 
    # CS2107 (fulfilled only by Computer Security fa)
    # and CS2101 (fulfilled by general requirements)
    # In general, there are too many restrictions to take IS4010.
    # As the special semester are not yet considered in the schedule,
    # I just omit IS4010 here.
    # TR3202 propose a mapping bewteen College of Design and Engineering
    # and School of Computing.
    # The searched results are all suggestions on mappings.
    # All the suggestions need department approval to take effects.
    # At the same time, TR3202 is not offered in this academic year.
    # Overall, TR3202 should not be counted as a general option to choose
    # for 6 month internship
    # I will just use CP3880 here.
    mod_mcs = 12
    have_intern = False
    pre1 = "CS2101"
    pre2 = "CS2103T"
    pre1T = False
    pre2T = False
    for i in range(0,16):
        # It is very rare to have internship in the first semester. 
        # So we consider internship starts from the second semester.
        if plan.sems[i].check_module_exist(pre1):
            pre1T = True
        if plan.sems[i].check_module_exist(pre2):
            pre2T = True
        if (not pre1T) or (not pre2T):
            continue
        if plan.sems[i].cur_mcs+mod_mcs<=plan.sems[i].max_mcs:
            plan.sems[i].modules.append("CP3880")
            plan.sems[i].cur_mcs += mod_mcs
            have_intern = True
            break
    if not have_intern:
        # simply take it to semester 7
        plan.sems[12].modules.append("CP3880")
        plan.sems[12].cur_mcs += mod_mcs

def intern3_1(plan:ModsPlan,intern2:bool):
    # There are two kinds of 3 month internship:
    # complete special term industry internship (CP3200, CP3202)
    # and social welfare internship (CP3107, CP3100)
    # However, CP3107 requires CS2030, which has preclusion
    # for basic course CS2030S.
    # So we omit it here.
    sem_intern = 0
    mod_mcs = 6
    have_intern = False
    # CP 3200 does not require any prerequisite
    for i in range(2,16,4):
        if plan.sems[i].cur_mcs+mod_mcs<=plan.sems[i].max_mcs:
            plan.sems[i].modules.append("CP3200")
            plan.sems[i].cur_mcs += mod_mcs
            have_intern = True
            sem_intern = i
            break
    if not have_intern:
        sem_intern = 10
        if intern2:
            sem_intern = 6
        plan.sems[sem_intern].modules.append("CP3200")
        plan.sems[sem_intern].cur_mcs += mod_mcs
    return sem_intern

def intern3_2(plan:ModsPlan, previntern):
    mod_mcs = 6
    have_intern = False
    # CP 3200 does not require any prerequisite
    for i in range(2,16,4):
        if previntern <= i:
            continue
        if plan.sems[i].cur_mcs+mod_mcs<=plan.sems[i].max_mcs:
            plan.sems[i].modules.append("CP3202")
            plan.sems[i].cur_mcs += mod_mcs
            have_intern = True
            break
    if not have_intern:
        plan.sems[10].modules.append("CP3202")
        plan.sems[10].cur_mcs += mod_mcs


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
        intern3_1(plan,False)
    if is3Month2Internships:
        intern1num = intern3_1(plan,True)
        intern3_2(plan,intern1num)
