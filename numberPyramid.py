
def print_number_pyramid(n):
    for i in range(1, n + 1):
        # Print spaces before the numbers
        for j in range(n - i):
            print(" ", end=" ")
        
        # Print numbers in ascending order
        for j in range(1, i + 1):
            print(j, end=" ")
        
        # Print numbers in descending order
        for j in range(i - 1, 0, -1):
            print(j, end=" ")
        
        # Move to the next line for the next 
        print()

try:
    n = int(input("Enter the number of rows for the pyramid: "))
    print_number_pyramid(n)
except ValueError:
    print("Please enter a valid number.")


"""
output:-
        1 
      1 2 1 
    1 2 3 2 1 
  1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1 

"""
