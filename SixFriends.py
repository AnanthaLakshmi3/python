# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if 3*x <=2*y:
        print(3*x)
    else:
        print(2*y)