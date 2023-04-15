# main function for generate module plan
# return json form of plan

import json

from . import generateplan
from .Sections import ULR, FAs, IDCD, QET, UE, internfyp
from .modsplan import ModsPlan



def modsplanner(request):
    
    # process the request to obtain id, major, fas
    req_dict = json.load(request)
    id = req_dict['id']
    major = req_dict['major']
    fas = req_dict['fas']  #fas:[{"name":"string","module":["string"]}]
    isFyp = req_dict['isFyp']
    is6MInt = req_dict['is6MonthInternship']
    is3M1Int = req_dict['is3Month1Internship']
    is3M2Int = req_dict['is3Month2Internships']
    maxMcs = req_dict['maxMcs']
    doesNeedQet = req_dict['doesNeedQet']
    cdIdGroup = req_dict['cdIdGroup']

    plan = ModsPlan(id)

    # University level requirements(24units): 
    ULR.add_ULR_modules(plan)

    # add Computing Ethics (4 units): IS1108
    CE = ['IS1108']

    # Computer Science Foundation (36units)
    CSF = ['CS1231S','CS2030S','CS2040S','CS2100','CS2101','CS2103T','CS2106','CS2109S','CS3230'] 

    # Math & Science (12unis)
    MS = ['MA1521','MA2001','ST2334'] 

    # process fas (20/24 units)
    FA = FAs.generate_fas_mods(fas,['CS1101S']+CE+CSF+MS)

    # add QET
    QET.newQET(plan,doesNeedQet)

    # generate schedule
    generateplan.generate_plan(plan,mods_list=['CS1101S']+CE+CSF+MS+FA)

    # process internship/fyp
    internfyp.add_special_sem(plan)
    internfyp.intern_fyp(plan,isFyp,is6MInt,is3M1Int,is3M2Int)

    # add ID/CD (12units)
    IDCD.add_idcd(plan,cdIdGroup)

    # add UE (40units)
    # need to substract excess mods selected in fas
    UE.add_UE(plan)

    # check degree requirement
    if plan.get_cur_mcs() >= 160:
        print("This plan meets all degree requirements!")

    return plan.ModsPlan_json()

