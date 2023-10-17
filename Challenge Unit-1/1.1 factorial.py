def factorial(n):
  if n < 0:
    print("Enter a valid number")
  elif n == 0:
    print("Factorial of 0 is 1")
  else:
    f = 1
    for i in range(1, n + 1):
      f = f * i
    print("The factorial is", f)


n = int(input("Enter a number: "))
factorial(n)
