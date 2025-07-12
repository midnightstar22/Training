n = int(input())
l1 = list(map(int, input().split()))

se = set(l1)
length = len(se)

if length != n:
    print("true")
else:
    print("false")
