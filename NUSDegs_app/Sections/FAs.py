# Process user's request for FAs

import re

from .. import module, prerequisites

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
FAs_mods = {'Algorithms & Theory': 
            {'Primaries':['CS3230', 'CS3231', 'CS3236', 'CS4231', 'CS4232', 'CS4234'], 
            'Electives':['CS3233', 'CS4257', 'CS4261', 'CS4268', 'CS4269', 'CS4330', 'CS5230', 'CS5234', 'CS5236', 'CS5237', 'CS5238', 'CS5330']}, 
        'Artificial Intelligence': 
            {'Primaries':['CS2109S', 'CS3263', 'CS3264', 'CS4243', 'CS4244', 'CS4246', 'CS4248'], 
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
            {'Primaries': ['CS2103T', 'CS3213', 'CS3219', 'CS4211', 'CS4218', 'CS4239'], 
            'Electives': ['CS3216', 'CS3217', 'CS3226', 'CS3234', 'CS5219', 'CS5232', 'CS5272']},
        'others':['CS2220', 'CS5233']
        }


def get_mods_level(mod_list):
    # obatin the levels of mods in mod_list
    levels = [int(re.search(r'\d',mod).group()) for mod in mod_list]
    return levels

def add_mods(num,mod_list,pre_mods):
    # add num mods from mod_list according to prerequisite based on pre_mods
    num -= len(set(mod_list)&set(pre_mods))
    if num <=0 :
        return []
    adds = []
    flag = 0
    for mod in mod_list:
        if mod in pre_mods:
            continue
        # if mod is preclusion of any mod in pre_mod: continue
        if prerequisites.check_mod_prereq(pre_mods,module(mod)):
            adds.append(mod)
            pre_mods.append(mod)
            num -= 1
        if num == 0:
            flag = 1
            return adds
    if flag == 0:
        for mod in list(set(mod_list)-(set(mod_list)&set(adds))):
            adds.append(mod)
            pre_mods.append(mod)
            num -= 1
            # add prerqe course
            prereqmods = prerequisites.add_prereq(pre_mods,module(mod))
            adds += prereqmods
            pre_mods += prereqmods
            for mod in prereqmods:
                if mod in mod_list:
                    # prereq mod is from mod_list
                    num -= 1
            if num <= 0:
                return adds


def level_4000_mods(mod_list):
    levels = get_mods_level(mod_list)
    idx = levels.index(4)
    mods4000 = mod_list[idx:]
    return mods4000


def process_user_mods(user_mods,pre_mods):
    # add user specified modules and its prereq mods
    adds = []
    for mod in user_mods:
        if mod in pre_mods:
            continue
        adds.append(mod)
        pre_mods.append(mod)
        if prerequisites.check_mod_prereq(pre_mods,module(mod))==False:
            # add mods that in prereq but not in pre_mods into fa_mods
            addmods = prerequisites.add_prereq(pre_mods,module(mod))
            adds += addmods
            pre_mods += addmods
    return adds


def add_primaries(fa,mods_list,pre_mods,n4):
    # check if current mods_list meet requirements and add primaries mods
    # add n4 level 4000 in primaries
    fa_mods_pri = FAs_mods[fa]['Primaries']
    if all(level<4 for level in get_mods_level(mods_list)):
        # add n4 level 4000 mod
        mods4000_pri = level_4000_mods(fa_mods_pri)
        addmods = add_mods(n4,mods4000_pri,pre_mods)
        mods_list += addmods
    # 3 primaries
    if len(set(mods_list)&set(fa_mods_pri))<3:
        num_toadd = 3 - len(set(mods_list)&set(fa_mods_pri))
        addmods = add_mods(num_toadd,list(set(fa_mods_pri)-(set(mods_list)&set(fa_mods_pri))),pre_mods)
        mods_list += addmods
    return mods_list


def generate_fas_mods(fas,pre_mods):
    #fas:[{"name":"string","module":["string"]}]
    fa_mods = []
    if len(fas) == 1:
        # set 3 primaries mods and 2 random mods for this fa
        fa = fas[0]['name']
        user_mods = fas[0]['module']   # module codes ["string"]
        fa_mods_pri = FAs_mods[fa]['Primaries']
        fa_mods_ele = FAs_mods[fa]['Electives']
        if user_mods != []:
            # add user specified modules and its prereq mods
            fa_mods += process_user_mods(user_mods,pre_mods)
            # add primaries mods
            fa_mods = add_primaries(fa,fa_mods,pre_mods,1)
            # add 2 level 4000 electives
            mods4000_ele = level_4000_mods(fa_mods_ele)
            num_toadd = 2-len(set(mods4000_ele)&set(fa_mods))
            addmods = add_mods(num_toadd,list(set(mods4000_ele)-(set(mods4000_ele)&set(fa_mods))),pre_mods)
            fa_mods += addmods

        else:
            # user has no specified modules
            mods4000_ele = level_4000_mods(fa_mods_ele)
            fa_mods = add_primaries(fa,[],pre_mods,1)
            num_toadd = 2-len(set(mods4000_ele)&set(fa_mods))
            fa_mods += add_mods(num_toadd,list(set(mods4000_ele)-(set(mods4000_ele)&set(fa_mods))),pre_mods)       
    if len(fas) == 2:
        # set 3 primaries mods for each fa
        num_4000 = 0
        for i in range(2):
            cur_fa_mods = []
            fa = fas[i]['name']
            user_mods = fas[i]['module']
            n4 = 1
            if num_4000==1: 
                # select only 1 4000 mod from fa_1
                # need to select 2 4000 mods form fa_2
                n4 = 2
            if user_mods!=[]:
                # user mods
                cur_fa_mods += process_user_mods(user_mods,pre_mods)
                # primaries mods
                cur_fa_mods = add_primaries(fa,cur_fa_mods,pre_mods,n4) 
            else: 
                cur_fa_mods = add_primaries(fa,[],pre_mods,n4)
            fa_mods += cur_fa_mods 
            # count num of level 4000 mods
            num_4000 = get_mods_level(fa_mods).count(4)

    return fa_mods

