# Declaring a python dictionary(associative array)(map) to store Fibonacci values that have been calculated
# This serves as our look-up table
fibonacci_cache = {}

# Function to calculate the nth term of the Fibonacci Sequence
# If n = 1 or 2, F(n) = 1
# If n > 2, F(n) = F(n - 1) + F(n - 2)
def calculateFibonacci(n):

    # If the input parameter is not an int
    if type(n) != int:

        # Display an error message on the console
        raise TypeError("'n' must be a positive int")
    
    # Input parameter is not a positive number
    if n < 1:

        # Display an error message on the console
        raise TypeError("'n' must be a positive int")

    # Checks if the specified index, n, has been stored in the map 
    if n in fibonacci_cache:

        # Returns the value stored at index 'n' in the look-up table
        return fibonacci_cache[n]
    
    # If the 1st number in the sequence is requested (Base case #1)
    if n == 1:
    
        # Sets the value to correspond with the 1st element
        value = 1

    # If the 2nd number in the sequence is requested (Base case #2)
    elif n == 2:
        
        # Sets the value to correspond with the 2nd element
        value = 1

    # If requested term is past the 2nd term
    elif n > 2:

        # Returns the sum of the previous two(2) terms
        value =  calculateFibonacci(n - 1) + calculateFibonacci(n - 2)

    # Stores the calculated value in the look-up table
    fibonacci_cache[n] = value

    # Returns the value to end the function
    return value

# For loop to run 100 times
for n in range(1, 101):

    # Outputs the nth Fibonacci number
    print(n, ":", calculateFibonacci(n))
