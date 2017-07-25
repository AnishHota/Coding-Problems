a,b = map(int,input().strip().split())
diff = a-b
if diff%10==9:
    result=diff-1
else:
    result=diff+1
print(result)
