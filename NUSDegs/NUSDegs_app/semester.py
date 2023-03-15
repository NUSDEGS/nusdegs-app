import module

class semester:
    # define the class of semester data

    def __init__(self,seq_num,max_mcs):
        # info for a semester
        seq_num = seq_num
        modules = []
        max_mcs = max_mcs
        cur_mcs = 0

    def add_module(self,mod:module):
        #add a module to this semester
        self.modules.append(mod)
        cur_mcs += mod.mcs 

    def if_under_maxmcs(self):
        # check if current mcs exceed maxmcs
        if self.cur_mcs > self.max_mcs:
            return False
        else :
            return True
    
