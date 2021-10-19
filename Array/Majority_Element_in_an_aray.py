def majority_element(a,n):
    maj_index=0
    count=1
    for i in range(1,n):
        if(a[maj_index]==a[i]):
            count+=1
        else:
            count-=1
        if count==0:
            maj_index=i
            count=1
    return maj_index

def ismajority_element(a,n,maj_elem):
    count=0
    for i in range(n):
        if a[i]==maj_elem:
            count+=1
    return (count>n//2)


from array import *
a=array('i',[])
n=int(input("Length of an array: "))
for i in range(n):
    x=int(input("Enter array elements: "))
    a.append(x)


maj_elem=a[majority_element(a,n)]

result= ismajority_element(a,n,maj_elem)
if result==True:
    print("Majority element is : ",maj_elem)
else:
    print("Majority element not found!")
