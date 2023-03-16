# generate ULR modules list

import random
from django.core.cache import cache

def ULR_modules():
    ULR = []
    # add Digital Literacy & Critique and Expression
    ULR.append('CS1101S','ES2660')
    # add Data Literacy 
    ULR.append(random.sample(['GEA1000','BT1101','ST1131','DSA1101'],1))
    # add Cultures and Connections
    GEC = cache.get('GEC%')
    ULR.append(random.sample(GEC,1))
    # add Singapore Studies
    GES = cache.get('GES%')
    ULR.append(random.sample(GES,1))
    # add Communities and Engagement
    GEN = cache.get('GEN%')
    ULR.append(random.sample(GEN,1))

    return ULR