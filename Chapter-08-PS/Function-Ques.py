        # Question No 1
# def greater(a,b,c):
#     if(a > b and a > c):
#         return a
#     elif(b > a and b > c):
#         return b
#     elif(c > a and c > b):
#         return c

# a: int = int(input("Enter Number A: "))
# b: int = int(input("Enter Number B: "))
# c: int = int(input("Enter Number C: "))

# print(f"The Largest Number of Function is {greater(a,b,c)}")


        # Question No 2
def convert(f):
    return 5 * (f-32) / 9
f: int = int(input("Enter Your Temperature: "))
c = convert(f)
print(f"{round(c, 2)}°C")