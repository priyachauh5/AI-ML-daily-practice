# s=input("Enter the String: ")
# i=0
# j=len(s)-1
# is_pal=True
# while i<j:
#     if s[i]!=s[j]:
#         is_pal=False
#         break
#     i+=1
#     j-=1

# if is_pal:
#     print("String is palindrome")
# else:
#     print("String is not palindrome")
# print(str)

s = input("Enter the string: ")

# Reverse the string and compare
if s == s[::-1]:
    print("String is palindrome")
else:
    print("String is not palindrome")
