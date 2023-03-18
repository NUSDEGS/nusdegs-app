import prerequisites

mod_list = ['b','y']
prereq_tree = {'and':[
    {'or':['a','b','c']},
    {'or':['c','d','e']},
    {'and':[{'or':['g','h']},
            'f']},
    {'or':[{'or':['t','k']},
           {'and':['r','y','z']}]}
    ]}
missing = prerequisites.add_prereq_helper(mod_list,prereq_tree)
missing = prerequisites.flatten(missing)
print(missing)