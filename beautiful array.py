test_case = int(input())
for i in range(test_case):
    n = int(input())
    nu = list(map(int,input().split(' ')))
    negative,one,other=0,0,0
    for num in nu:
        if num==-1:
            negative+=1
        elif num==1:
            one+=1
        elif num!=0:
            other+=1
    if other>=2 or (negative>0 and other==1) or (negative>1 and one==0):
        print('no')
    else:
        print('yes')
