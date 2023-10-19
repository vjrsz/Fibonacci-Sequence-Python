from fibonacci_bottomup import fibonacci_bottomup
from fibonacci_recursive import fibonacci_recursive
from fibonacci_topdown import fibonacci_topdown

if __name__ == "__main__":
    # = 3
    print(fibonacci_topdown(3))
    print(fibonacci_recursive(3))
    print(fibonacci_bottomup(3))

    # = 8
    print(fibonacci_recursive(6))
    print(fibonacci_recursive(6))
    print(fibonacci_bottomup(6))
