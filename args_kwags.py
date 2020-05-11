# def funargs(a,b,c,d):
#     print(a,b,c,d)

# a="hi"
# b='hello'
# c='how'
# d='are you'
# e='fine'
# funargs(a,b,c,d)
# funargs(a,b,c,d,e)

#it gives error
#def funargs(*args,normal):
def funargs(normal,*args,**kwags):
    print(normal)
    print(args)
    for key,value in kwags.items():
        print(f"{key}  {value}")


names = ["hi","hello","how are you"]
nrmal="this is normal"
kw ={"name":'gautam',
      "batch":'A'   
    }
funargs(nrmal,*names,**kw)
funargs(nrmal)
#funargs(*name,nrmal):error
