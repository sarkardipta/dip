def check_odd_even(number):
    if number % 2 == 0:
        return f"{number} is Even"
    else:
        return f"{number} is Odd"


number = int(input("Enter a number: "))
result = check_odd_even(number)
print(result)
