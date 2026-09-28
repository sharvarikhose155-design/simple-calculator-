def add(a, b):
    return a + b


def divide(a, b):
    return a / b


def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)


def main():
    print("Simple Calculator")

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Addition:", add(a, b))
    print("Division:", divide(a, b))

    numbers = [a, b]
    print("Average:", calculate_average(numbers))


if __name__ == "__main__":
    main()
