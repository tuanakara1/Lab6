global sum
sum = 0


def series(n, k):
    global sum
    if k == n + 1:

        return
    else:
        term = (-1) ** (k + 1) / k
        sum += term
        series(n, k + 1)

n = int(input("Enter value for n: "))

series(n, 1)

print("Sum of the series = ", sum)
