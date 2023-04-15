# define the class of modules
#from django.core.cache import cache
import requests
import re
from . import tags

class module:
    # class for modules

    def __init__(self,code):
        # get module info from redis database
        # keys: code, title. mcs, tags, info
        self.code = code
        self.tags = []
        if code=='UE':
            self.title = ""
            self.mcs = 4
            self.tags.append("Unrestricted Electives")
        else:
            #self.info = json.load(cache.get(code))
            url = 'https://api.nusmods.com/v2/2022-2023/modules/'+code+'.json'
            self.info = {key:value for (key,value) in requests.get(url).json().items()}
            self.title = self.info['title']
            self.mcs = int(self.info['moduleCredit'])
        # add tags
        if code=='ES1000' or code=='ES1103':
            self.tags.append("English modules")
        if code=='CP3880' or code=='CP3200' or code=='CP3202':
            self.tags.append("Internship")
        if code=='CP4101':
            self.tags.append("FYP")
        if code in ['CS1101S','ES2660','GEA1000','BT1101','ST1131','DSA1101'] or code.startswith('GEC') or code.startswith('GES') or code.startswith('GEN'):
            self.tags.append("University level requirements")
        if code=='IS1108':
            self.tags.append("Computing Ethics")
        if code in ['CS1231S','CS2030S','CS2040S','CS2100','CS2101','CS2103T','CS2106','CS2109S','CS3230']:
            self.tags.append("Computer Science Foundation")
        if code in ['MA1521','MA2001','ST2334']:
            self.tags.append("Math & Science")
        if code in tags.fas_mods:
            self.tags.append("CS Focus Area")
        if code in tags.idcd_mods:
            self.tags.append("Interdisciplinary/Cross Disciplinary")
        
        


    def semester(self):
        # get the semester nums which the module is offered
        sem_data = self.info['semesterData']
        sems_availabel = []
        for sem in sem_data:
            sems_availabel.append(int(sem['semester']))
        return sems_availabel
      

    def prerequisite(self):
        # get prerequisite modules in prereqTree format
        if 'prerequisiteRule' not in self.info.keys():
            return {}
        prereqrule = self.info['prerequisiteRule']
        prereq_tree = self.generate_prereqtree(prereqrule)
        return prereq_tree
    

    def preclusion(self):
        # get preclusion modules
        preclurule = self.info['preclusionRule']
        preclumods = re.findall(r"\b[A-Z]{2,4}\d{4}[A-Z]?\b",preclurule)
        return preclumods


    def module_json(self):
        # response dict
        response = {
            "code":self.code,
            "title":self.title,
            "mcs":self.mcs,
            "tags":self.tags
        }
        return response
    

    def generate_prereqtree(self,prereqrule):
        # generate prereqTree from prereqrule
        tokens = re.findall(r"\(\d+\)|\(|\)|AND|OR|\b[A-Z]{2,4}\d{4}[A-Z]?\b",prereqrule)   
        tokens = self.preprocess_tokens(tokens) 
        prereq_tree = self.parse_tokens(tokens,0)
        return prereq_tree
    

    def preprocess_tokens(self,tokens):
        # add () to AND relations
        if tokens[0]!='(':
            tokens = ['(']+tokens+[')']
        stack = []
        pre_left = []
        pre_right = []
        pre_sub_str = []
        for i, c in enumerate(tokens):
            if c == '(':
                stack.append(i)
            elif c == ')':
                left_pos = stack.pop()
                right_pos = i
                if pre_left==[] and pre_right==[]:
                    sub_tokens = tokens[left_pos+1:right_pos]
                elif pre_right[-1]<left_pos:
                    sub_tokens = tokens[left_pos+1:right_pos]
                else:
                    sub_tokens = ['()']+tokens[pre_right.pop()+1:right_pos]
                    while len(pre_right)>0 and pre_right[-1]>left_pos:
                        sub_tokens = ["()"]+tokens[pre_right.pop()+1:pre_left.pop()] + sub_tokens
                    sub_tokens = tokens[left_pos+1:pre_left.pop()]+sub_tokens  
                if 'OR' in sub_tokens and 'AND' in sub_tokens:
                    or_groups = ' '.join(sub_tokens).split('OR')
                    for i,group in enumerate(or_groups):
                        if 'AND' in group and group[0]!='(':
                            or_groups[i] = '('+group+')'
                    new_sub_str = '('+'OR'.join(or_groups)+')'
                else: 
                    new_sub_str = '('+' '.join(sub_tokens)+')'
                if '()' in new_sub_str:
                    while len(pre_sub_str)>len(pre_left):
                        last_idx = new_sub_str.rfind('()')
                        left = new_sub_str[:last_idx]
                        right = new_sub_str[last_idx+len('()'):]
                        new_sub_str = left + pre_sub_str.pop() + right
                pre_sub_str.append(new_sub_str)
                pre_left.append(left_pos)
                pre_right.append(right_pos)
        new_tokens = re.findall(r"\(\d+\)|\(|\)|AND|OR|\b[A-Z]{2,4}\d{4}[A-Z]?\b",new_sub_str)
        return new_tokens                     

    def parse_tokens(self,tokens,pos):
        # helper func for generate prereqTree
        tree = {}
        cur = []
        flag = -1 # 0 for or, 1 for and
        while pos <= len(tokens):
            if pos==len(tokens):
                if flag:
                    tree['and'].append(cur)
                else:
                    tree['or'].append(cur)
                return tree
            if tokens[pos] == ')':
                pos += 1
                if tree == {}:
                    return cur,pos
                else:
                    if flag:
                        tree['and'].append(cur)
                    else:
                        tree['or'].append(cur)
                    return tree,pos
            elif tokens[pos] == '(':
                pos += 1
                cur,pos = self.parse_tokens(tokens,pos)
                if pos == len(tokens):
                    return cur
            elif re.match(r'\(\d+\)',tokens[pos]):
                num = int(re.findall(r'\d+',tokens[pos])[0])
                if num == 1:
                    orlist = []
                    pos += 1
                    while pos<len(tokens) and re.match(r'\b[A-Z]{2,4}\d{4}[A-Z]?\b',tokens[pos]):
                        orlist.append(tokens[pos])
                        pos += 1
                    cur = {'or':orlist}
                else :
                    andlist = []
                    pos += 1
                    while pos<len(tokens) and re.match(r'\b[A-Z]{2,4}\d{4}[A-Z]?\b',tokens[pos]):
                        andlist.append(tokens[pos])
                        pos += 1
                    cur = {'and':andlist}
            elif tokens[pos] == 'AND':
                pos += 1
                flag = 1
                if tree == {}:
                    tree['and'] = [cur]
                else :
                    tree['and'].append(cur)
            elif tokens[pos] == 'OR':
                pos += 1
                flag = 0
                if tree == {}:
                    tree['or'] = [cur]
                else :
                    tree['or'].append(cur)
           
    """
    def generate_prereq_combinations(self,prereq_tree):
        #helper function for prerequisite
        if isinstance(prereq_tree, str):
            return [prereq_tree]
        else:
            combinations = []
            for operator, operands in prereq_tree.items():
                if operator == "and":
                    operand_combinations = [self.generate_prereq_combinations(op) for op in operands]
                    combinations = [list(combo) for combo in itertools.product(*operand_combinations)]
                elif operator == "or":
                    for operand in operands:
                        combinations += self.generate_prereq_combinations(operand)
        return combinations   
    """