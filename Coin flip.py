t = int(input())
for _ in range(t):
    g =  int(input())
    for _ in range(g):
        i,n,q = map(int,input().strip().split())
        if i==1:
            if q==1:
                result=n//2
            else:
                if n%2==0:
                    result=n//2
                else:
                    result=(n//2)+1
        else:
            if q==1:
                if n%2==0:
                    result=n//2
                else:
                    result=(n//2)+1
            else:
                result = (n//2)
        print(result)
