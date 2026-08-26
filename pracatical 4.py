fact= int(input("enter a number for factorial"))
factorial=1
for i in range(1,fact+1):
    factorial=factorial*i
print("factorial of",fact,"is",factorial)

fact=1
def factorial(a):
  global fact
  if a>1:
    fact = fact*a
    factorial(a-1)

  else:
    return
num =int(input("enter a number for factorial"))
factorial(num)
print("factorial of",num,"is",fact)

