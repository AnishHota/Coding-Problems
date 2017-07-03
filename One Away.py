string1 = input()
string2 = input()
count=0
for i in set(string1):
    if string1.count(i)!=string2.count(i):
        count+=1
if count<=1:
    print('True')
else:
    print('False')
