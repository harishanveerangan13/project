# # reverse a number using the while loop
#
# num1 = int(input("The number you want to reverse: "))
# num2 = int(input("The number you want it to end at: "))
# num3 = int(input("The amount you want to reverse by: "))
#
# while num1 > num2:
#     print(num1 - num3)
#     num1 = num1 - num3
#
# # prime number check whether given number is a prime number
#
# num = int(input("Enter number:  "))
# if num > 1:  # check whether number is greater than one since prime numbers > 1
#     for i in range(2, num): #chooses range of numbers between number of choice and 2
#         if (num % i) == 0:  #divides from the range of numbers and checks whether remainder is 0
#             print(num, "is not a prime number")
#             print(i, "times", num // i, "is", num) #shows why number is not prime
#             break  # this ends the loop
#     else:
#         print(num, "is a prime number")
# else:
#     print("Number is not a prime number because it is not greater than 1")
#
#
# #code that prints alphabets a-z
#
#
# x = int(input("Enter the number: "))
# reverse = 0
#
#
# while (x != 0):
#     rem = x % 10
#     reverse = reverse*10+rem
#     x = x//10
#
# print(reverse) #step 1 x = 123  reverse = 0 then 123 != 0 true rem = 3 reverse = 0*10+3 x = 123//10 x = 12

#step 2 x = 12 true rem = 2 reverse = 32 then x = 12//10 x = 1 then

#step 3 x = 1 rem = 1 % 10  reverse = 32*10+1 = 321 1//10 = 0.000... x = 0 final value is 321