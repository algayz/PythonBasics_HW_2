try:
    sumNumbers = int(input("Введите сумму двух натуральных чисел: "))
    multiplicationNumbers = int(input("Введите произведение двух натуральных чисел: "))
    if sumNumbers < 0 or multiplicationNumbers < 0:
        print("Введено отрицательное значение")
    else:
        discriminant = sumNumbers ** 2 - 4 * multiplicationNumbers
        if discriminant < 0:
            print(f"Задача не имеет решения")            
        else:
            if discriminant == 0:
                numberFirst = sumNumbers / 2
                numberSecond = sumNumbers - numberFirst
            else:
                numberFirst = (sumNumbers - discriminant ** 0.5) / 2
                numberSecond = (sumNumbers + discriminant ** 0.5) / 2
            if numberFirst == int(numberFirst) and numberSecond == int(numberSecond):
                print(f"Загаданы натуральные числа: {int(numberFirst)} и {int(numberSecond)}")       
            else:
                print(f"Нет натуральных чисел, которые бы отвечали условию задачи")
except:
    print("Введено не допустимое значение")