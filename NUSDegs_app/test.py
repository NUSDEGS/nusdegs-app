from module import module
import prerequisites
import itertools
import re
import FAs

fas = [{
    'name':'Computer Graphics and Games',
    'module':[]
},{
    'name':'Software Engineering',
    'module':[]
}]

pre_mods = ['CS1101S','IS1108','CS1231S','CS2030S','CS2040S','CS2100','CS2101','CS2103T','CS2106','CS2109S','CS3230','MA1521','MA2001','ST2334']

FA = FAs.generate_fas_mods(fas,pre_mods)
print(FA)
