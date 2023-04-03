# generate ULR modules list

import random
from django.core.cache import cache

def add_ULR_modules(plan):
    # add Data Literacy 
    DL = random.sample(['GEA1000','BT1101','ST1131','DSA1101'],1)[0]
    plan.add_module(0,DL)
    # add Cultures and Connections
    GEC = 'GEC1017'
    plan.add_module(1,GEC)
    #GEC = random.sample(cache.get('GEC%'),1)
    # add Singapore Studies
    GES = 'GES1005'
    plan.add_module(2,GES)
    #GES = random.sample(cache.get('GES%'),1)
    # add Communities and Engagement
    GEN = 'GEN2000'
    plan.add_module(3,GEN)
    #GEN = random.sample(cache.get('GEN%'),1)
    # add Critique and Expression
    CriEx = 'ES2660'
    plan.add_module(3,CriEx)
    
