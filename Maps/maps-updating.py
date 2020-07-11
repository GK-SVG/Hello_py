import collections

dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day4': 'Thu'}

res = collections.ChainMap(dict1, dict2)

print(res.maps,'\n')

dict2['day4'] = 'Fri'

print(res.maps,'\n')