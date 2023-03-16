# Process user's request for FAs

import module,semester,modsplan
import prerequisites
import itertools
import re

"""
# obtain fas and relavant modules from web

import requests
from bs4 import BeautifulSoup

# send request to url and parse with BeautifulSoup
url = 'https://www.comp.nus.edu.sg/programmes/ug/focus/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# get the modules of each FA and store into dict
course_dict = {}
article_body = soup.find_all('div',{'itemprop': 'articleBody'})[0]

current_fa = None  # current focus area
for element in article_body.children:
    if element.name == 'h3':  # next focus area
        current_fa = element.text.strip()
        course_dict[current_fa] = {'Primaries': [], 'Electives': []}  
    elif current_fa is not None:  # if processing current focus area
        if element.name == 'h3':  # stop when encounter focus area
            current_fa = None
        if element.name == 'ul' and flag==1 :
            primaries = []
            for subelem in element:
                if subelem.name == 'li':
                    primaries.append(subelem.next.text.strip())
            course_dict[current_fa]['Primaries'].extend(primaries)  # add to Primaries list
        if element.name == 'ul' and flag==0 :
            electives = []
            for subelem in element:
                if subelem.name == 'li':
                    electives.append(subelem.next.text.strip())
            course_dict[current_fa]['Electives'].extend(electives)  # add to Electives list
        elif element.name == 'p':  # process Primaries or Electives modules
            if element.text.strip().startswith('Primaries'):
                flag = 1                
            elif element.text.strip().startswith('Electives'):
                flag = 0

print(course_dict)
"""

# FAs dict obtained
FAs = {'Algorithms & Theory': 
            {'Primaries':['CS3230', 'CS3231', 'CS3236', 'CS4231', 'CS4232', 'CS4234'], 
            'Electives':['CS3233', 'CS4257', 'CS4261', 'CS4268', 'CS4269', 'CS4330', 'CS5230', 'CS5234', 'CS5236', 'CS5237', 'CS5238', 'CS5330']}, 
        'Artificial Intelligence': 
            {'Primaries':['CS2109S', 'CS3243', 'CS3244', 'CS3263', 'CS3264', 'CS4243', 'CS4244', 'CS4246', 'CS4248'], 
             'Electives': ['CS4220', 'CS4261', 'CS4269', 'CS4277', 'CS4278', 'CS5215', 'CS5228', 'CS5242', 'CS5260', 'CS5340', 'CS5339']}, 
        'Computer Graphics and Games': 
            {'Primaries':['CS3241', 'CS3242', 'CS3247', 'CS4247', 'CS4350'], 
            'Electives':['CS3218', 'CS3240', 'CS3249', 'CS4240', 'CS4243', 'CS4249', 'CS4351', 'CS5237', 'CS5240', 'CS5343', 'CS5346']}, 
        'Computer Security': 
            {'Primaries': ['CS2107', 'CS3235', 'CS4236', 'CS4230', 'CS4238', 'CS4239'], 
            'Electives': ['CS3221', 'CS4257', 'CS4276', 'CS5231', 'CS5250', 'CS5321', 'CS5322', 'CS5331', 'CS5332', 'IFS4101', 'IFS4102', 'IFS4103']}, 
        'Database Systems': 
            {'Primaries': ['CS2102', 'CS3223', 'CS4221', 'CS4224', 'CS4225'], 
            'Electives': ['CS4220', 'CS5226', 'CS5228', 'CS5322']}, 
        'Multimedia Information Retrieval': 
            {'Primaries': ['CS2108', 'CS3245', 'CS4242', 'CS4248', 'CS4347'], 
            'Electives': ['CS5246', 'CS5241']}, 
        'Networking and Distributed Systems': 
            {'Primaries': ['CS2105', 'CS3103', 'CS4222', 'CS4226', 'CS4231'], 
            'Electives': ['CS3237', 'CS4344', 'CS5223', 'CS5224', 'CS5229', 'CS5248', 'CS5321']}, 
        'Parallel Computing': 
            {'Primaries': ['CS3210', 'CS3211', 'CS4231', 'CS4223'], 
            'Electives': ['CS5222', 'CS5223', 'CS5224', 'CS5239', 'CS5250']}, 
        'Programming Languages': 
            {'Primaries': ['CS2104', 'CS3211', 'CS4212', 'CS4215'], 
            'Electives': ['CS3234', 'CS4216', 'CS5232', 'CS5214', 'CS5215', 'CS5218']}, 
        'Software Engineering': 
            {'Primaries': ['CS2103', 'CS2103T', 'CS3213', 'CS3219', 'CS4211', 'CS4218', 'CS4239'], 
            'Electives': ['CS3216', 'CS3217', 'CS3226', 'CS3234', 'CS5219', 'CS5232', 'CS5272']},
        'others':['CS2220', 'CS5233']
        }


def get_mods_level(mod_list):
    # obatin the levels of mods in mod_list
    levels = [int(re.search(r'\d',mod).group()) for mod in mod_list]
    return levels



def generate_fas_mods(fas):
    # fas:["string"]
    # user chooses 1 fa
    if len(fas)==1 :
        # randomly pick 5 modules from this fa
        fa_all_mods = FAs[fas[0]]['primaries']+FAs[fas[0]]['electives']
        for combo in itertools.combinations(fa_all_mods, 5):
            # check if contains >=3 in primaries
            pri = list(set(combo)&set(FAs[fas[0]]['primaries']))
            if len(pri) < 3:
                continue
            # check if contain >=1 level 4000 in primaries
            level_pri = get_mods_level(pri)
            if all(level<4 for level in level_pri):
                continue
            # check if contains >=3 level 4000
            levels = get_mods_level(fa_all_mods)
            if sum(level>=4 for level in levels) < 3:
                continue
            # if meets all requirements
            return combo
    #user chooses 2 fas
    if len(fas)==2:
        # randomly pick 3 mods from each fa_primaries
        for combo1 in itertools.combinations(FAs[fas[0]],3):
            # check if contains >=1 level 4000 in fa1
            level_1 = get_mods_level(combo1)
            if all(level<4 for level in level_1):
                continue
            for combo2 in itertools.combinations(FAs[fas[0]],3):
                # check if contains >=1 level 4000 in fa2
                level_2 = get_mods_level(combo2)
                if all(level<4 for level in level_2):
                    continue
                #check if contains >=3 level 4000 in fa1+fa2
                levels = get_mods_level(combo1+combo2)
                if sum(level>=4 for level in levels) < 3:
                    continue
                return combo1+combo2


def process_fas(plan:modsplan,fas,pre_mods):
    while True:
        FA = generate_fas_mods(fas)
        cur_mods = pre_mods + FA
        # check if all prerequisite met 
        if prerequisites.check_prerequisites(cur_mods):
            # add mods into plan
            plan.generate_plan()
            return
        else :
            continue

    