word = "процент"
num = 0
while num < 100 :
    num += 1
    if (num % 10 == 0 or
            num == 11 or
            num == 12 or
            num == 13 or
            num == 14 or
            5 <= num % 10 <= 9):
        print(num, word + "ов")
    elif 2 <= num % 10 < 5:
        print(num, word + "a")
    elif num % 10 == 1:
        print(num, word)