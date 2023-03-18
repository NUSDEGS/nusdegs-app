from module import module
import prerequisites

mod = module('CS4243')
flag = mod.prerequisite()
#pre_mods = ['CS1101S','IS1108','CS1231S','CS2030S','CS2040S','CS2100','CS2101','CS2103T','CS2106','CS2109S','CS3230','MA1521','MA2001','ST2334']
#res = prerequisites.check_prereqTree(pre_mods,flag)
print(flag)

prerequisiteRule="PROGRAM_TYPES IF_IN Undergraduate Degree THEN COURSES (1) CS2040:D, CS2040C:D, CS2040S:D, YSC2229:D AND (COURSES (1) EE2012A:D, EE2012:D, YSC2243:D AND COURSES (1)ST2131:D, ST2334:D OR COURSES (2) MA2116:D, MA2216:D) AND (COURSES (2) MA1511:D, MA1512:D OR COURSES (1) MA2001:D, MA1101R:D AND COURSES (1) MA2002:D, MA1521:D, MA1102R:D)"
