from math import floor, log2


def count(n: int) -> None:
    # Precondition: n > 0.
    p = floor(log2(n)) + 1 # The number of bits required to represent n.
    bits = [0] * p # Initialize an array of length p with all 0’s.

    for i in range(n): # i = 0, 1, ..., n-1
        # Increment the current count in the bits array. This adds 1 to
        # the current number, basically using the loop to act as a "carry" operation.
        j = p - 1
        while bits[j] == 1:
            bits[j] = 0
            j -= 1
        bits[j] = 1


