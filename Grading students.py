n=int(input())
for i in range(n):
    mark = int(input())
    if mark<38:
        print(mark)
    elif mark%5>=3:
        mark+=(5-mark%5)
        print(mark)
    else:
        print(mark)
