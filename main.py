# Fibonacci Bottom Up
def fibonacci_recursive(n):
    if n <= 2:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Fibonacci Top Down
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


# MAIN
if __name__ == "__main__":
    print(fibonacci_topdown(3))  # = 3
    print(fibonacci_recursive(3))  # = 3

    print(fibonacci_recursive(6))  # = 8
    print(fibonacci_recursive(6))  # = 8
