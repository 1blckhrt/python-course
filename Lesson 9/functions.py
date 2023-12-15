def hello_world():
    print("Hello World!")

hello_world()

def sum(num1 = 0, num2 = 0):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2

total = sum()
print(total)

