        # Question 01
# n = int(input("Enter Your Number: "))

# for i in range(1,11):
#     print(f"{n} + {i} = {n*1}")


        # Question 02
# l = ["Harry", "Soham", "Sachin", "Rahul"]

# for name in l:
#     if(name.startswith("S")):
#         print(f"Hello {name}")


        # Question 03
# n = int(input("Enter Your Number: "))

# i = 1
# while i < 11:
#     print(f"{n} + {i} = {n*i}")
#     i += 1


        # Question 04
# n = int(input("Enter Your Number: "))

# for i in range(2,n):
#     if(n%i == 0):
#         print("Number not is prime")
#         break
# else:
#         print("Number is prime")


        # Question 05
# n = int(input("Enter Your Number: "))
# i = 1
# sum = 0

# while(i <= n):
#     sum += i
#     i += 1
#     print(sum)


        # Question 06
n = int(input("Enter the number: "))
product = 1
for i in range(1, n+1):
    product = product * i

print(f"The factorial of {n} is {product}")