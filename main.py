def cube(num):
    print(num**3)
def divisible(num):
    remainder = num%3
    if remainder == 0:
        cube(num)
    else:
        print("This number is not divisible by 3")
num = int(input("Enter a number: "))
divisible(num)