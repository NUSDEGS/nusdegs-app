from . import module

def check_prerequisites(mod_list):
    # check if all prerequisites met for mods in mod_list
    for mod in mod_list:
        if check_mod_prereq(mod_list,mod)==False:
            return False
    return True


def is_prereq_of(mod1,mod2):  #mod1,mod2: string
    # check if mod1 is preqreq mod of mod2
    prereqTree = module(mod2).prerequisite()
    return is_in_prereqTree(mod1,prereqTree)


def is_in_prereqTree(mod,prereqTree):
    # check if mod in prereqTree
    # helper func for is_prereq_of
    if prereqTree=={}:
        return False
    if isinstance(prereqTree,str):
        return mod==prereqTree
    else: 
        for andor,options in prereqTree.items():
            if options==[]:
                return False
            else: 
                return any(is_in_prereqTree(mod,op) for op in options)


def check_mod_prereq(mod_list,mod:module):
    # check if current mod_list meets the prerq of mod
    prereq_tree = mod.prerequisite()    
    return check_prereqTree(mod_list,prereq_tree)


def check_prereqTree(mod_list,prereq_tree):
    # check if mod_list meet prereq tree
    # helper func fot check_mod_prereq
    if prereq_tree=={}:
        return True
    if isinstance(prereq_tree,str):
        return prereq_tree in mod_list
    else:
        for andor,options in prereq_tree.items():
            if options==[]:
                return True
            if andor=='and':
                return all(check_prereqTree(mod_list,op) for op in options)
            elif andor=='or':
                return any(check_prereqTree(mod_list,op) for op in options)

def add_prereq(mod_list,mod:module):
    # check if current mod_list meets the prerq of mod and return prereq mods needed
    missing_mods = []
    prereq_tree = mod.prerequisite() 
    adding_mods = add_prereq_helper(mod_list,prereq_tree)
    adding_mods = flatten(adding_mods)
    missing_mods += adding_mods
    while any(check_mod_prereq(mod_list,module(amod))==False for amod in adding_mods):
        to_check = adding_mods
        adding_mods = []
        for amod in to_check:
            adding_mods += add_prereq(mod_list,module(amod))
            missing_mods += adding_mods
    return missing_mods

def add_prereq_helper(mod_list,prereq_tree):
    if isinstance(prereq_tree,str):
        if prereq_tree in mod_list:
            missing_mods = []
        else:
            missing_mods = prereq_tree
        return missing_mods
    else:
        for andor,options in prereq_tree.items():
            if andor=='and':
                missing_mods = []
                for op in options:
                    missing_mods += [add_prereq_helper(mod_list,op)]
            elif andor=='or':
                optional_mods = []
                flag = 0
                for op in options:
                    missing_mods = add_prereq_helper(mod_list,op)
                    if missing_mods == []:
                        flag = 1
                        break
                    else :
                        optional_mods += [missing_mods]
                if flag==1:
                    missing_mods = []
                else:
                    if optional_mods==[]:
                        missing_mods = []
                    else:
                        missing_mods = [optional_mods[0]]
            return missing_mods

def flatten(lst):
    result = []
    for elem in lst:
        if isinstance(elem, list):
            result.extend(flatten(elem))
        else:
            result.append(elem)
    return result