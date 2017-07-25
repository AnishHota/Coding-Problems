t = int(input())
for _ in range(t):
    n,m = map(int,input().strip().split())
    completed = list(map(int,input().split()))
    incomplete=[]
    for i in range(1,n+1):
        if i not in completed:
            incomplete.append(int(i))
    chef = incomplete[::2]
    assist = incomplete[1::2]
    for x in chef:
        print(x,end=' ')
    if len(chef)==0:
        print(' ')
    print()
    for y in assist:
        print(y,end=' ')
    if len(assist)==0:
        print(' ')
