def print_inverse_number_pyramid(n):
    for i in range(n, 0, -1):
        # Print spaces before the numbers
        for j in range(n - i):
            print(" ", end=" ")

        # Print numbers in descending order
        for j in range(i, 0, -1):
            print(j, end=" ")

        # Move to the next line for the next 
        print()

try:
    n = int(input("Enter the number of rows for the inverse pyramid: "))
    print_inverse_number_pyramid(n)
except ValueError:
    print("Please enter a valid number.")


"""
output:-

5 4 3 2 1 
  4 3 2 1 
    3 2 1 
      2 1 
        1 

"""
