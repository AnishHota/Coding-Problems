string1 = input()
string2 = input()
flag=0
if len(string1)!=len(string2):
    flag=1
for i in string1:
    if string1.count(i)!=string2.count(i):
        flag=1
if flag==0:
    print('Permutation')
else:
    print('No Permutation')
