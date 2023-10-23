def print_number_diamond(n):
    if n % 2 == 0:
        n += 1

    for i in range(1, n + 1, 2):
        spaces = (n - i) // 2
        numbers = list(range(1, i + 1))

        # Print leading spaces
        print(" " * spaces, end="")

        # Print numbers in increasing order
        for num in numbers:
            print(num, end="")

        # Print numbers in decreasing order, excluding the last number
        for num in reversed(numbers[:-1]):
            print(num, end="")

        # Print trailing spaces and move to the next line
        print(" " * spaces)

if __name__ == "__main__":
    n = int(input("Enter the number of rows for the diamond pattern: "))
    print_number_diamond(n)
"""
output:-
Enter the number of rows for the diamond pattern: 5
  1  
 121 
12321
 121 
  1  


"""
