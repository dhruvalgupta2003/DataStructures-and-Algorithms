def findpairs(a,n,sum):
    mydict=dict()
    for i in range(0,n):
        temp=sum-a[i]
        if(temp in mydict):
            count=mydict[temp]
            for j in range(count):
                print("Pairs are : ","(",temp,",",a[i],")",sep=" ",end="\n")
                
        if a[i] in mydict:
            mydict[a[i]]+=1
        else:
            mydict[a[i]]=1

from array import *
a=array('i',[])
n=int(input("Length of an array: "))
for i in range(n):
    x=int(input("Enter array elements: "))
    a.append(x)
sum=6
findpairs(a,n,sum)
