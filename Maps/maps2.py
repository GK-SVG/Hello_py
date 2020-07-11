import collections

dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day4': 'Thu'}

res1 = collections.ChainMap(dict1, dict2)

print(res1.maps,'\n')

res2 = collections.ChainMap(dict2, dict1)

print(res2.maps,'\n')