# cook your dish here
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    p=a+c
    q=a+d 
    r=b+c 
    s=b+d 
    print(max(p,q,r,s))