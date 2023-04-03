IDCD_groups = {
    'Management and IT':['IS1128','IS2218','DAO2703'],
    'Molecular Biology':['HSI1000','HSI2003','HSI2004'],
    'Human Studies':['HSH1000','HSS1000','SC1101E'],
    'Astrophysics':['HSI1000','HSI2009','HSI2010','HSI2011'],
    'Design':['DTK1234','EG1311','EG2201A'],
    'History of Science':['HSI1000','HSI2005','HSI2008'],
    'Medical Science':['HSI1000','HSI2001','HSI2014']
}

idcd_mods = sum(IDCD_groups.values(),[])


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
        }

fas_mods = []
for val in FAs_mods.values():
    fas_mods += sum(val.values(),[])

