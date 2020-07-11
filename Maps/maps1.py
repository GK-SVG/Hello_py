import collections

dict1={'day1':'Monday','day2':'Tuesday'}
dict2={'day3':'Thursday','day4':'Wednesday','day1':'Sunday'}

res= collections.ChainMap(dict1,dict2)

#As a tuple of dictonary
print(res)

#as a list of dictionry
print(res.maps)

print('Keys={}'.format(tuple(res.keys())))
print('Values={}'.format(tuple(res.values())))
print('Keys={}'.format(list(res.keys())))
print('Values={}'.format(list(res.values())))


for key , val in res.items():
    print('{}={}'.format(key,val))
print()

