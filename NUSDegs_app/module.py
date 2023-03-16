# define the class of modules
from django.core.cache import cache

class module:
    # class for modules

    def __init__(self,code):
        # get module info from redis database
        # keys: code, title. mcs, tags
        self.code = code
        self.tags = []
        value = cache.get(code)
        #process value to get tile, mcs ,tags
        pass
    
    def add_tag(self,tag:str):
        # add a tag for module
        self.tags.append(tag)


    def semester(self,value):
        # get the semester nums which the module is offered
        pass

    def prerequisite(self,value):
        # get prerequisite modules
        pass
    
    def corequisite(self,value):
        # get corequisite modules
        pass
    
    def preclusion(self,value):
        # get preclusion modules
        pass

    def timeslot(self,value):
        # check if the module is available in morning/afternoon/evening
        pass
    