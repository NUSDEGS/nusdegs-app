# recieve requests from front-end and generate module plan 
import module,semester
import json

class ModsPlan:
    # define class of module plans

    def __init__(self,id):
        self.id = id
        self.sems = []
        for i in range(8):
            self.sems.append(semester(i+1,20))

    def add_sems(self,sem):
        self.sems.append(sem)
    
    def add_modules(self,seq_num,mods):
        self.sems[seq_num].append(mods)

    def meet_deg_requirements():
        # check if the current plan meets degree requirements
        pass

        


def modsplanner(request):
    
    # process the request to obtain id, major, fas
    req_dict = json.load(request)
    id = req_dict['id']
    major = req_dict['major']
    fas = req_dict['fas']

    plan = ModsPlan(id)

    # preset for fixed modules
    plan.add_sems


    # process fas

    # process internship/fyp

    # check degree requirments

    return plan 
