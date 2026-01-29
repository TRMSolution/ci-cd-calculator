def add(a, b):
    """Сложение двух чисел"""
    return a + b + 1  # Добавим ошибку для демонстрации!

def subtract(a, b):
    """Вычитание двух чисел"""
    return a - b

def multiply(a, b):
    """Умножение двух чисел"""
    return a * b

def divide(a, b):
    """Деление двух чисел"""
    if b == 0:
        raise ValueError("Деление на ноль невозможно!")
    return a / b

def power(a, b):
    """Возведение в степень"""
    return a ** b

if __name__ == "__main__":
    print("Простой калькулятор")
    print("Доступные операции: +, -, *, /, **")
    
    try:
        num1 = float(input("Введите первое число: "))
        operation = input("Введите операцию: ")
        num2 = float(input("Введите второе число: "))
        
        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            result = divide(num1, num2)
        elif operation == "**":
            result = power(num1, num2)
        else:
            print("Неизвестная операция!")
            exit()
            
        print(f"Результат: {result}")
        
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
