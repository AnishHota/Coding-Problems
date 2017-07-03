string = input()
count=0
for i in string:
    if string.count(i.lower())%2!=0 and i!=' ':
        count+=1
length = len([1 for i in string if i!=' '])
if length%2!=0 and count==1:
    print('Permutation of a Palindrome')
elif length%2==0 and count==0:
    print('Permutation of a Palindrome')
else:
    print('Not a Permutation of a Palindrome')
