def solve(k,i,a):
    if(len(a)==1):
        return a[0]
    i=(i+k)%len(a)
    a.pop(i)
    return solve(k,i,a)
        
n=int(input())
k=int(input())
i=0
a=[i+1 for i in range(n)]

    
x=solve(k-1,i,a)
print(x)
