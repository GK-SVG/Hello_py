ptr=open('gk.txt')
ptr2=open('as.txt')
ptr3=open('asi.txt')
def inputData():
    print('1 for Gk Diet')
    print('2 for Gk Diet')
    print('3 for Gk Diet')
    num=int(input("Enter Person no:"))
    return num

ch = inputData()
if ch==1:
    print(ptr.read())
elif ch==2:
    print(ptr2.read())
elif ch==3:
    print(ptr3.read())
ptr.close()
ptr2.close()
ptr3.close()

