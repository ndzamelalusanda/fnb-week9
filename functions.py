...
def greet(name):
    print("hello,{name}")   
    # This function greets the user by name.
    greet("Alice")  
    # Example usage of the greet function.
    # The function is called with the name "Alice".
    # The output will be: hello,Alice
    def add(a, b):
        return a + b
    # This function adds two numbers and returns the result.
    result = add(2, 5)
    print(result)
    # The result will be 7.
...
   
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    # This function calculates the factorial of a number recursively.
    # Example: factorial(5) will return 120.  
def greet(name, greeting="hello"):
    print(f"{greeting}, {name}")
    # This function greets the user with a customizable greeting.
    # Example usage: greet("Alice", "hi") will output "hi, Alice".
    # If no greeting is provided, it defaults to "hello".
    
greet("Bob","Good morning")
    # Example usage of the greet function with a custom greeting.
    # The output will be: good morning, Bob