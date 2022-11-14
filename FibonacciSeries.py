def fibonacci_recursive(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


n = int(input('Enter a number: \n'))
print(fibonacci_recursive(n))


def fibonacci_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i + 1)
    return fac


n = int(input('Enter a number: \n'))
print(fibonacci_iterative(n))


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input('Enter a number: \n'))
print(factorial(n))
