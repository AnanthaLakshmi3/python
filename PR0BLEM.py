# cook your dish here
T = int(input())
for i in range(T):
    N,M=map(int,input().split())
    if abs((N-M))%2==0:
        print("YES")
    else:
        print("NO")