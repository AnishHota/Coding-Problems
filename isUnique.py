n = input()
flag=1
for i in n:
    if n.count(i)>1:
        flag=0
if flag==0:
    print('Not unique')
else:
    print('Unique')
