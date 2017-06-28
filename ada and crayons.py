testCase = int(input())
for _ in range(testCase):
    seq = input()
    if seq[0]=='U':
        result=seq.count('UD')
    else:
        result=seq.count('DU')
    print(result)
