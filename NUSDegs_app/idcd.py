from modsplan import ModsPlan
from module import module

IDCD_groups = {
    'Management and IT':['IS1128','IS2218','DAO2703'],
    'Molecular Biology':['HSI1000','HSI2003','HSI2004'],
    'Human Studies':['HSH1000','HSS1000','SC1101E'],
    'Astrophysics':['HSI1000','HSI2009','HSI2010','HSI2011'],
    'Design':['DTK1234','EG1311','EG2201A'],
    'History of Science':['HSI1000','HSI2005','HSI2008'],
    'Medical Science':['HSI1000','HSI2001','HSI2014']
}


def add_idcd(plan:ModsPlan,interest:str):
    # given plan with special semester now
    # we will add all of the courses in the interested idcd group
    courses = IDCD_groups[interest]
    total_c_n = len(courses)
    j = 0
    mod_mcs = 4
    cur_course = module(courses[j])
    sem = cur_course.semester()
    i = 2
    while (i <= 16):
        if (plan.sems[i].cur_mcs+mod_mcs<=plan.sems[i].max_mcs) and (((i % 4) + 1) in sem):
            plan.sems[i].modules.append(courses[j])
            plan.sems[i].cur_mcs += mod_mcs
            j += 1
            if j == 1:
                i += 1 # the first course may be a pre-req
                # update if it is the first course
            if j == total_c_n:
                # all courses are added
                break
            
        else:
            i += 1 # move forward if max_mcs is overloaded
