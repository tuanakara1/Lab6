from math import factorial

n = int(input("Enter value for n: "))
x = int(input("Enter value for x: "))

term = lambda i: (n ** i) / factorial(i)

sum = 1

for i in range(1, x+1):
    sum += term(i)

print("e^n = ", sum)
