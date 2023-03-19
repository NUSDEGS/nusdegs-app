# define class for module plans
from module import module
from semester import semester
import prerequisites

class ModsPlan:
    # define class of module plans

    def __init__(self,id):
        self.id = id
        self.sems = []
        for i in range(8):
            self.sems.append(semester(i+1,20))
    
    def add_module(self,seq_num,mod):
        #  aadd a module to a semester
        self.sems[seq_num].modules.append(mod)

    def meet_deg_requirements(self):
        # check if the current plan meets degree requirements
        all_mods = []
        prerequisites.check_prerequisites(all_mods)
        pass
    
    def ModsPlan_json(self):
        # response dict
        response = {
            'id':self.id,
            'sems':[sem.semester_json() for sem in self.sems]
        }
        return response