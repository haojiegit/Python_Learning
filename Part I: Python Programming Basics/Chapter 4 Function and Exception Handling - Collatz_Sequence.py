def collatz(number):
    """
    Generate the Collatz sequence starting from a given number.

    Parameters:
    number (int): The starting number for the Collatz sequence.

    Returns:
    If number is even, the collatz() should print number // 2 and 
    return this value. If number is odd, the collatz() should 
    print and return 3 * number + 1.

    """
    try:
        number = int(number)
        if number <= 0:
            raise ValueError("Input must be a positive integer.")
      
        while number != 1:
            print(number, end=" ")
            if number % 2 == 0:
               number = number // 2
            else:
               number = 3 * number + 1
        print(number)  # Print the final number (1) in the sequence
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        return None

number = input("Enter a positive integer: ")
collatz(number)