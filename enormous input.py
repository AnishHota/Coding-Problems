inp = list(map(int,input().split()))
n = inp[0]
k = inp[1]
count=0
for i in range(n):
    x = int(input())
    if x%k==0:
        count+=1
print(count)
