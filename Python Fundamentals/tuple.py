nums = (1, 2, 3, 4, 5, 6, 7, 8, 9)

even_tuple = ()
odd_tuple = ()

for n in nums:
    if n % 2 == 0:
        even_tuple += (n,)
    else:
        odd_tuple += (n,)

print("Even numbers tuple:", even_tuple)
print("Odd numbers tuple:", odd_tuple)
