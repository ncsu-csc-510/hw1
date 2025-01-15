def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    # print("Factorial of 5:", factorial(5))
    print("Factorial of -3:", factorial(-3))  

if __name__ == "__main__":
    main()
