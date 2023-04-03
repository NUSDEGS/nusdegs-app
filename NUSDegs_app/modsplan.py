# define class for module plans
from module import module
from semester import semester
import prerequisites

class ModsPlan:
    # define class of module plans

    def __init__(self,id,maxMcs):
        self.id = id
        self.sems = []
        self.sems.append(semester(1,20))
        for i in range(1,4):
            self.sems.append(semester(i+1,maxMcs))
        for i in range(4,8):
            self.sems.append(semester(i+1,20))
    
    def add_module(self,seq_num,mod:str):
        # add a module to a semester
        self.sems[seq_num].modules.append(mod)
        self.sems[seq_num].cur_mcs += module(mod).mcs

    def get_cur_mcs(self):
        # calculate cur mcs of plan
        plan_mcs = 0
        for sem in self.sems:
            plan_mcs += sem.cur_mcs
        return plan_mcs
    
    def ModsPlan_json(self):
        # response dict
        response = {
            'id':self.id,
            'sems':[sem.semester_json() for sem in self.sems]
        }
        return response