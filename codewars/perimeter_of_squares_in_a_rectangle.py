def perimeter(n):
    # your code
    n += 1
    if n <= 0:
        return 0

    fibo = [0] * (n + 1)
    fibo[1] = 1

    total_sum = fibo[0] + fibo[1]

    for i in range(2, n + 1):
        fibo[i] = fibo[i - 1] + fibo[i - 2]
        total_sum += fibo[i]

    return total_sum * 4
