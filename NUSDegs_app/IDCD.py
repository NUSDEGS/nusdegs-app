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
    for mod in courses:
        cur_mod = module(mod)
        mod_mcs = cur_mod.mcs
        sem = cur_mod.semester()
        for i in range(16):
            if (plan.sems[i].cur_mcs+mod_mcs<=plan.sems[i].max_mcs) and (((i % 4) + 1) in sem):
                plan.sems[i].modules.append(mod)
                plan.sems[i].cur_mcs += mod_mcs
                break
            