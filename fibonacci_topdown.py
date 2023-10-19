global vector


def fibonacci_topdown(n):
    global vector

    if n <= 2:
        return 1

    vector = [-1] * (n + 1)
    (vector[1], vector[2]) = (1, 1)

    for i in range(3, n):
        vector[i] = -1

    return fibonacci_recursive_topdown(n)


def fibonacci_recursive_topdown(n):
    global vector
    if vector[n] == -1:
        vector[n] = fibonacci_recursive_topdown(n - 1) + fibonacci_recursive_topdown(n - 2)
    return vector[n]