testCase = int(input())
while testCase>0:
    inp = list(map(int,input().split()))
    a = inp[0]
    b = inp[1]
    n = inp[2]
    if n%2==0:
        print(max(a,b)//min(a,b))
    else:
        print(max(a*2,b)//min(a*2,b))
    testCase-=1
