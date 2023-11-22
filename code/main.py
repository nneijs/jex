def my_print(*args, end='\n', sep=' '):
    # Loop through each argument
    for arg in args:
        # Convert the argument to a string and print it
        # (Assuming str() can handle each data type)
        print(str(arg), end=sep)

    # Print a newline character at the end (default behavior)
    print(end, end='')

# Example usage of the custom print function
my_print("Hello", "World", 42, 3.14)