A=[8,7,9,0,7,8,8,0,9,4]
A.sort()
print(A)
print(sum(A))
print(len(A))
print(min(A),"and",max(A))
print(A.count(min(A)), "and", A.count(max(A)))
A.pop(min(A))
print(A)
A.remove(max(A))
print(A)