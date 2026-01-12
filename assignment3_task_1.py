def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Call the function with a sample number
factorial_number = int(input("Enter a number: "))
output = factorial(factorial_number)

print(f"Factorial of {factorial_number} is: {output}")
