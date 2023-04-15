from . import module

class semester:
    # define the class of semester data

    def __init__(self,seq_num,max_mcs):
        # info for a semester
        self.seq_num = seq_num
        self.modules = []
        self.max_mcs = max_mcs
        self.cur_mcs = 0


    def add_module(self,mod):
        #add a module to this semester
        self.modules.append(mod)
        self.cur_mcs += module(mod).mcs 


    def if_under_maxmcs(self):
        # check if current mcs exceed maxmcs
        return self.cur_mcs < self.max_mcs
    

    def semester_json(self):
        # response_dict 
        response = {
            'seq_num':self.seq_num,
            'modules':[module(mod).module_json() for mod in self.modules]
        }
        return response
    
    def check_module_exist(self,mod_code):
        for one_mod in self.modules:
            if one_mod == mod_code:
                return True
        return False
