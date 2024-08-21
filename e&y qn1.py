n = int(input())
m = set(map(int,input().split()))
print(type(m))
even = []
odd = []
for i in range(len(m)):
    if i % 2 == 0:
        even.append(m[i])
    else:
        odd.append(m[i])
print(sum(even))