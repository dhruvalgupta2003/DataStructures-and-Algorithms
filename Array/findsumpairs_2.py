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

a=[1,5,7,-1,5]
n=len(a)
sum=6
findpairs(a,n,sum)