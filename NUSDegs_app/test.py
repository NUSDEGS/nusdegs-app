import re

pri = ['CS3230', 'CS3231', 'CS3236', 'CS4231', 'CS4232', 'CS4234']
level_pri = [int(re.search(r'\d',mod).group()) for mod in pri]

print(level_pri)