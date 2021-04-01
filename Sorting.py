import math
def InsertSort(a):
    for i in range(len(a)):
        x = a[i]
        j = i-1
        while j>=0 and a[j] >x:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=x
    return a

def Merge(b,c):
    d=[]
    d.append(b)
    d.append(c)
    i=0
    j=0
    for k in range(len(d)-1):
        if b[i] <c[j]:
            d[k] = b[i]
            i=i+1
        else:
            d[k] = c[j]
            j=j+1
    return d

def mergeSort(a,m,n):
    if n-m ==1:
        return [a[m]]
    else:
        p = (n+m)//2
        b = mergeSort(a,m,p)
        c = mergeSort(a,p,n)
        d = Merge(b,c)
        return d

def mergeSortAll(a):
    return mergeSort(a,0,len(a))
