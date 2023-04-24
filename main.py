def square_and_concatenate_digits(number):
    # сначала мы просто сохраняем в переменную номер как писанину
    number_str = str(number)
    # Создаем зачем то пустую строку
    result = ""
    # В новой переменной которая будет цифровой в будущем (щас нет) сохраняем все значения от буквенной переменной
    for digit_str in number_str:
        # чтобы нам работать и как то умножать нам же нужно привести ту самую цифровую переменную в реально цифровную
        digit = int(digit_str)
        # Далее мы просто возводим в степень
        squared_digit_str = str(digit ** 2)
        # здесь сложно для меня понять но в тот самый разультат мы добавляем ту шнягу от квадратной
        result += squared_digit_str
    # Теперь наш любимыый результат мы переводим в цифру
    result = int(result)
    return result
print(square_and_concatenate_digits(7734))