def integer_number():
    try:
        number = int(input())
    except:
        return 0
    else:
        return number


print(integer_number())
