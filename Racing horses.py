t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int,input().split()))
    s.sort(reverse=True)
    mi = abs(s[0]-s[1])
    for i in range(n-1):
        if s[i]-s[i+1]<mi:
            mi = s[i]-s[i+1]
    print(mi)
