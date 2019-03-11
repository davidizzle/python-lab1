print("Input the string that shall be abbreviated.")
word = input()

cnt = len(word)

if cnt < 2:
    print("String is empty")

else:
    str1 = word[0]+word[1]
    str2 = word[cnt-2] + word[cnt-1]
    str = str1+str2
    print(str)

