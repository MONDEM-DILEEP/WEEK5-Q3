#with recursion

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

num = int(input("Enter a number: "))
print("Factorial (with recursion):", fact(num))


#without recursion

n = int(input("Enter a number: "))
factorial = 1
if n < 0:
    print("Factorial is not defined for negative numbers")
else:
    for i in range(1, n + 1):
        factorial *= i
    print("Factorial (without recursion)", n, "is", factorial)

