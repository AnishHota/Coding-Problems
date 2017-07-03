string = input()
result=''
flag = string[0]
for i in range(len(string)):
    if string[i]!=flag or i==0:
        result+=string[i]
        flag = string[i]
        count=1
        j=i+1
        while j<len(string) and string[j]==string[i] :
            count+=1
            j+=1
        result+=str(count)
if len(result)<len(string):
    print(result)
else:
    print(string)
