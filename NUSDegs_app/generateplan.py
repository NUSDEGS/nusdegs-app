import networkx as nx
from collections import deque

from . import module, prerequisites
from .modsplan import ModsPlan
from .Sections import FAs

def DAG(mods_list):   #mods_list: list of module codes ['string']
    # generate DAG
    G = nx.DiGraph()
    level_mods = [[],[],[],[],[]]
    levels = FAs.get_mods_level(mods_list)
    for idx,level in enumerate(levels):
        level_mods[level-1].append(mods_list[idx])
    for k,list in enumerate(level_mods):
        for i,cur_mod in enumerate(list):
            G.add_node(cur_mod)
            for pre_list in level_mods[:k+1]:
                for j,other_mod in enumerate(pre_list):
                    if other_mod!=cur_mod and prerequisites.is_prereq_of(other_mod,cur_mod):
                        G.add_edge(other_mod,cur_mod)
    return G


def arrange_mods(plan:ModsPlan,G):
    # arrange mods from DAG into each semester
    in_degree = {node: 0 for node in G}
    sem_prereq_clear = {node:-1 for node in G}
    for node in G:
        for neighbor in G[node]:
            in_degree[neighbor] += 1
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    while queue:
        node = queue.popleft()
        # skip CS2101
        if node=='CS2101':
            continue
        mod_node = module(node)
        mod_mcs = mod_node.mcs
        sem_num = mod_node.semester()
        for i in range(sem_prereq_clear[node]+1,8): 
            cur_sem = i % 2 + 1
            if cur_sem in sem_num:
                if plan.sems[i].cur_mcs+mod_mcs<=plan.sems[i].max_mcs:
                    plan.sems[i].modules.append(node)
                    plan.sems[i].cur_mcs += mod_mcs
                    break
        if node=='CS2103T':
            plan.sems[i].modules.append('CS2101')
            plan.sems[i].cur_mcs += 4
        for neighbor in G[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                sem_prereq_clear[neighbor]= i
                queue.append(neighbor)
    return 


def generate_plan(plan:ModsPlan,mods_list):
    #create DAG from mods_list
    dag = DAG(mods_list)
    # arrange mods
    arrange_mods(plan,dag)
    return