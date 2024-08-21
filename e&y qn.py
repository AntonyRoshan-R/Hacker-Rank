n = input()
m = int(input())
b = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range (len(b)):
    if b[i] == n:
        i = (i + m) % 26
        print(b[i])
    