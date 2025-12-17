# def goodDay(name, ending):
#     print("Good Day, " + name)
#     print(ending)
#     return "ok"

# a = goodDay("Faizan", "Thank You")
# goodDay("Amna", "Thank You")
# goodDay("Ali", "Thank You")

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter Your Number: "))
print(f"The Factorial Number is {factorial(n)}")