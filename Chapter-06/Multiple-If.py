a = int(input("Enter Your Age: "))

# If Statement No 01 Start

if a%2 == 0:
    print("A is Even")

# If Statement No 01 End

# If Statement No 02 Start

if a >= 18:
    print("You Are Eligible")
    print("Good For You")

elif a < 0:
    print("You Have Entered a Wrong Age")

elif a == 0:
    print("You Have Entered an Invalid Age")

else:
    print("You Are Not Eligible")
    
# If Statement No 02 End

print("End of Program")
