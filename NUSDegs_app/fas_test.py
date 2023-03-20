from module import module
from semester import semester
from modsplan import ModsPlan
import prerequisites
import itertools
import re
import FAs, generateplan
import matplotlib.pyplot as plt
import networkx as nx
import time

fas = [{
    'name':'Parallel Computing',
    'module':[]
},{
    'name':'Software Engineering',
    'module':['CS4239']
}]

pre_mods = ['CS1101S','IS1108','CS1231S','CS2030S','CS2040S','CS2100','CS2101','CS2103T','CS2106','CS2109S','CS3230','MA1521','MA2001','ST2334']

time1 = time.time()
FA = FAs.generate_fas_mods(fas,pre_mods)
#print(FA)
#print(pre_mods)
plan = ModsPlan(1)
#G = generateplan.DAG(pre_mods)
#nx.draw(G, with_labels=True)
#plt.show()
generateplan.generate_plan(plan,pre_mods)
time2 = time.time()
print(time2-time1)
print(plan.ModsPlan_json())

