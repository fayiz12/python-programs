n = int(input("Enter the number of rows (must be odd): "))

for i in range(1, n // 2 + 2):
    spaces = " " * (n // 2 + 1 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

for i in range(n // 2, 0, -1):
    spaces = " " * (n // 2 + 1 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
