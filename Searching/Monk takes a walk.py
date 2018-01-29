for _ in range(int(input())):
    vowels=['A','E','I','O','U','a','e','i','o','u']
    word = input()
    count=0
    for x in word:
        if x in vowels:
            count+=1
    print(count)
