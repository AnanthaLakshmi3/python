# cook your dish here
t=int(input())
for i in range(t):
    x=int(input())
    if(x>=1 and x<100):
        print("Easy")
    elif (x>=100 and x<200):
        print("Medium")
    else:
        print("Hard")