# define class for module plans
import module,semester
import prerequisites

class ModsPlan:
    # define class of module plans

    def __init__(self,id):
        self.id = id
        self.sems = []
        for i in range(8):
            self.sems.append(semester(i+1,20))

    def add_sem(self,sem):
        # add a semester plan
        self.sems.append(sem)
    
    def add_module(self,seq_num,mod:module):
        #  aadd a module to a semester
        self.sems[seq_num].append(mod)

    def meet_deg_requirements():
        # check if the current plan meets degree requirements
        all_mods = []
        prerequisites.check_prerequisites(all_mods)
        pass

    def generate_plan(mods_list):
        # arrange mods into plan according to prerequisites
        pass
