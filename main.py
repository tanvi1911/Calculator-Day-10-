#Calculator
from art import logo

def calculator():
  print(logo)
  def add(n1, n2):
    """It returns the sum of the given inputs"""
    return {n1 + n2}

  def subtract(n1, n2):
    """It returns the _____ of the given inputs"""
    return n1 - n2

  def multiply(n1, n2):
    """It returns the product of the given inputs"""
    return n1 * n2

  def division(n1, n2):
    """It returns the result after dividing the given inputs"""
    return n1 / n2


  operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply, 
    "/" : division
    }

  num1 = float(input("What's the first number? "))
  for symbol in operations:
    print(symbol)
  should_continue = True

  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number? "))
    
    operation_function = operations[operation_symbol]
    answer = operation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    if input("type 'y' to continue calculation and 'n' to exit: ").lower() == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()