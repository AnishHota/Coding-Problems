#I have to use matrix exponentian for this dynamic programming problem.
#Normal recursion and storing willn't work as this could go upto 10^18.
#Also,that the solution forms a fibonacci sequence.
#0->1,1->2,2->3,3->5 and so on.

f=[[1,1],[1,0]]
def multiply(f,m):
    a=(f[0][0]*m[0][0]+f[0][1]*m[1][0])%1000000007
    b=(f[0][0]*m[0][1]+f[0][1]*m[1][1])%1000000007
    c=(f[1][0]*m[0][0]+f[1][1]*m[1][0])%1000000007
    d=(f[1][0]*m[0][1]+f[1][1]*m[1][1])%1000000007

    f[0][0]=a%1000000007
    f[0][1]=b%1000000007
    f[1][0]=c%1000000007
    f[1][1]=d%1000000007
def func(n):
    m=[[1,1],[1,0]]
    if n==0 or n==1:
        return
    func(int(n/2))
    multiply(f,f)
    if n%2!=0:
        multiply(f,m)
for _ in range(int(input())):
    f=[[1,1],[1,0]]
    n = int(input())
    func(n+1)
    print(f[0][0]%1000000007)
