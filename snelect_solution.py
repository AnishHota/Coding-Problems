testCase = int(input())
for i in range(testCase):
    lineUp = input()
    mongooseCount = lineUp.count('m')
    lineUp = lineUp.replace('sm','').replace('ms','')
    snakesCount = lineUp.count('s')
    if mongooseCount>snakesCount:
        print('mongooses')
    elif snakesCount>mongooseCount:
        print('snakes')
    else:
        print('tie')
