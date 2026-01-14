input()
n = [*map(int, input().split())]
input()
m = [*map(int, input().split())]
n = set(n)
for e in m:
    if e in n:
        print(1)
    else:
        print(0)