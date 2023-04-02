# main function for generate module plan

from module import module
from semester import semester
from modsplan import ModsPlan
import ULR, FAs
import prerequisites, generateplan
import internfyp
import qet
import idcd
import json


def modsplanner(request):
    
    # process the request to obtain id, major, fas
    req_dict = json.load(request)
    id = req_dict['id']
    major = req_dict['major']
    fas = req_dict['fas']  #fas:[{"name":"string","module":["string"]}]

    isFyp = req_dict['isFyp']
    is6mintern = req_dict['is6MonthInternship']
    is31intern = req_dict['is3Month1Internship']
    is32Intern = req_dict['is3Month2Internships']
    maxMcs = req_dict['maxMcs']
    doesNeedQet = req_dict['doesNeedQet']
    cdIdGroup = req_dict['cdIdGroup']


    plan = ModsPlan(id,maxMcs)

    plan = ModsPlan(id)

    # University level requirements(24units): 
    ULR_ = ULR.ULR_modules()

    # add Computing Ethics (4 units): IS1108
    CE = ['IS1108']

    # Computer Science Foundation (36units)
    CSF = ['CS1231S','CS2030S','CS2040S','CS2100','CS2101','CS2103T','CS2106','CS2109S','CS3230'] 

    # Math & Science (12unis)
    MS = ['MA1521','MA2001','ST2334'] 

    # process fas (20/24 units)
    FA = FAs.generate_fas_mods(fas,ULR_+CE+CSF+MS)

    #generate schedule
    generateplan.generate_plan(plan,mods_list=ULR_+CE+CSF+MS+FA)

    # process internship/fyp

    internfyp.add_special_sem(plan)

    internfyp.intern_fyp(plan,isFyp,is6mintern,is31intern,is32Intern)
    qet.newQET(plan,doesNeedQet)


    # add ID/CD (12units)

    idcd.add_idcd(plan,cdIdGroup)


    # UE (40units)
    # need to substract excess mods selected in fas

    # check degree requirments

    return plan 
