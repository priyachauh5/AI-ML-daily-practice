#Average of Two Numbers
# a=float(input("Enter first number: "))
# b=float(input("Enter second number: "))
# average=(a+b)/2
# print("The average of",a,"and",b,"is",average)

# name=input("Enter your name: ")
# Age=int(input("Enter your age: "))
# print("Hello",name+"! You are",Age,"years old.")

# a=int(input("Enter the first number: "))
# b=int(input("Enter the second number: "))
# print("Sum:", int(a+b))
# print("Difference:", int(a-b))
# print("Product:", int(a*b))
# print("quotient:", int(a/b))

# a=int(input("Enter the first number: "))
# b=int(input("Enter the second number: "))
# c=float(input("Enter the first number: "))
# print(float(a+b+c)/3)

# a=(input("Enter the number: "))
# print(int(a))
# print(float(a))
# print(str(a))

# x=10+3*2**2
# print(x)

# a=int(input("Enter the first number: "))
# b=int(input("Enter the second number: "))
# print(a, b)
# c=a
# a=b
# b=c
# print(a,b)

# a=int(input("Enter the temperature: "))
# print(float(a*(9/4)+32))

# r=int(input("Enter the first number: "))
# pi=3.14
# print("Area is: ", float(pi*r**2))

# p=int(input("Enter the first number: "))
# r=int(input("Enter the second number: "))
# t=int(input("Enter the first number: "))
# print("Simple Interest is: ", float(p*r*t)/100)


# a=int(input("Enter the first number: "))
# b=int(input("Enter the second number: "))

# Take decimal number as input
num = input("Enter a decimal number: ")

# Split integer and fractional parts
if '.' in num:
    integer_part, fractional_part = num.split('.')
else:
    integer_part = num
    fractional_part = '0'

print("Integer part:", integer_part)
print("Fractional part: ." + fractional_part)
