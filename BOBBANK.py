# cook your dish here
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    p=b-c
    print(a+(p*d))