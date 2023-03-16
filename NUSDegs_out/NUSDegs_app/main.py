# main function for generate module plan

import module, semester, modsplan
import ULR, FAs
import prerequisites
import json






def modsplanner(request):
    
    # process the request to obtain id, major, fas
    req_dict = json.load(request)
    id = req_dict['id']
    major = req_dict['major']
    fas = req_dict['fas']

    plan = modsplan.ModsPlan(id)

    # University level requirements(24units): 
    ULR_ = ULR.ULR_modules()

    # add Computing Ethics (4 units): IS1108
    CE = ['IS1108']

    # Computer Science Foundation (36units)
    CSF = ['CS1231S','CS2030S','CS2040S','CS2100','CS2101','CS2103T','CS2106','CS2109S','CS3230'] 

    # Math & Science (12unis)
    MS = ['MA1521','MA2001','ST2334'] 

    # process fas (20/24 units)
    FAs.process_fas(plan,fas,pre_mods=ULR_+CE+CSF+MS)

    # process internship/fyp

    # add ID/CD (12units)

    # UE (40units)

    # check degree requirments

    return plan 
