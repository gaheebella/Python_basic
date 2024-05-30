def add(num1, num2):
    result = num1 + num2
    return result

def subtract(num1, num2):
    result = num1 - num2
    return result

def multiply(num1, num2):
    result = num1 * num2
    return result

def divide(num1, num2):
    result = num1 / num2
    return result

x = input("계산을 입력하세요(+,-,*,/) : ")

n1 = int(input("첫 번째 수를 입력하세요: "))
n2 = int(input("두 번째 수를 입력하세요: "))

if (x == "+"):
    y = add(n1, n2)
elif (x == "-"):
    y = subtract(n1, n2)
elif (x == "*"):
    y = multiply(n1, n2)
elif (x == "/"):
    y = divide(n1, n2)

print(f"##계산기 : {n1} {x} {n2} = {y}")
