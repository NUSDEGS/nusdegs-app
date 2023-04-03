from module import module
from semester import semester
from modsplan import ModsPlan
import prerequisites
import itertools
import re
import FAs, generateplan, QET, UE, ULR
import matplotlib.pyplot as plt
import networkx as nx
import time
import internfyp, IDCD

fas = [{
    'name':'Parallel Computing',
    'module':[]
},{
    'name':'Software Engineering',
    'module':['CS4239']
}]

time1 = time.time()
plan = ModsPlan(1,24)
ULR.add_ULR_modules(plan)
CE = ['IS1108']
CSF = ['CS1231S','CS2030S','CS2040S','CS2100','CS2101','CS2103T','CS2106','CS2109S','CS3230'] 
MS = ['MA1521','MA2001','ST2334'] 
FA = FAs.generate_fas_mods(fas,['CS1101S']+CE+CSF+MS)
QET.newQET(plan,True)
generateplan.generate_plan(plan,['CS1101S']+CE+CSF+MS+FA)
internfyp.add_special_sem(plan)
internfyp.intern_fyp(plan,False,False,False,True)
IDCD.add_idcd(plan,'Molecular Biology')
UE.add_UE(plan)
print(plan.ModsPlan_json())
time4 = time.time()
print(time4 - time1)
print(plan.get_cur_mcs())