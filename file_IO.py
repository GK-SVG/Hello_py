'''
"r"---open file fr read---default
"w"---open file fr write
"x"---create a file if not exist
"a"---add contant to a file
"t"---text mode---default
"b"---binary mode
'''

#ptr=open('gk.txt','rb')
# content=ptr.read()
# print(content)
# ptr=open('gk.txt','rt')
# content=ptr.read(4)
# print(content)
# content=ptr.read(4)
# print(content)
# print(ptr.readline())
# print(ptr.readline())
# print(ptr.readlines())
# for line in ptr:
#     print(line,end=" ")
# ptr = open('gk.txt','w')
# ptr.write('this is write which clear all content and write new content')
# ptr = open('gk.txt','a')
# ptr.write('this is apend which append new content\n')
ptr = open('gk.txt','r+')
print(ptr.read())
ptr.write('this function read sa well as write \n')
print(ptr.read())
ptr.close()