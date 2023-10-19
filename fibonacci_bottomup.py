def fibonacci_bottomup(n):
    if n <= 2:
        return 1

    vector = [0] * (n + 1)
    (vector[1], vector[2]) = (1, 1)
    for i in range(3, n + 1):
        vector[i] = vector[i - 1] + vector[i - 2]

    return vector[n]
