try:
    number = int(input("Введите число N: "))
    if number > 0:
        degree = 0
        twoDegree = 1
        print(f"Целые степени двойки до числа {number}:", end = " ")
        while twoDegree <= number:
            print(twoDegree, end = " ")
            degree += 1
            twoDegree = 2 ** degree      
    else:
        print("Введено не допустимое значение")
except:
    print("Введено не допустимое значение")