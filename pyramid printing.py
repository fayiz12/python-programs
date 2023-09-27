#     *
#    ***
#   *****
#  *******
# *********

def print_pyramid(height):
    for i in range(1, height + 1):
        # Print leading spaces
        print(" " * (height - i), end="")

        # Print stars
        print("*" * (2 * i - 1))

if __name__ == "__main__":
    try:
        height = int(input("Enter the height of the pyramid: "))
        if height <= 0:
            print("Please enter a positive integer.")
        else:
            print_pyramid(height)
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
