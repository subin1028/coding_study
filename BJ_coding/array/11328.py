n = int(input())
poss = []
for _ in range(n):
    st1, st2 = input().split()
    if sorted(st1) == sorted(st2):
        print("Possible")
    else:
        print("Impossible")