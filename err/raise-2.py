def divide_numbers(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        raise

    return result

try:
    print(divide_numbers(10, 0))
except:
    print("Error caught in the main block!")

