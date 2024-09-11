def prime(Number):
    """Check if a number is prime."""
    if Number > 1:
        for i in range(2, Number):
            if (Number % i) == 0:
                print(Number, "is not a Prime Number")
                break
        else:
            print(Number, "is a Prime Number")

prime(34)
