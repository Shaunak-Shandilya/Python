expression = []
print("enter X to finish",end = "\n\n")
while True:
    ch = input("Enter expression values : ")
    if ch.upper() == "X":
        break
    expression.append(ch)
i = 0
print("Entered expression = ",expression)

#FIRST PRIORITY ^ (Exponent)
while i < len(expression):
    if expression[i] == '^':
        expression[i] = int(expression[i-1]) ** int(expression[i+1])
        expression.pop(i-1)
        expression.pop(i)
        i=0
    else:
        i+=1
print(expression, end = "\n\n\n")
#SECEND PRIORITY * and / (Multiply and Divide)
i=0
while i < len(expression):
    if expression[i] == '*':
        expression[i] = int(expression[i-1]) * int(expression[i+1])
        expression.pop(i-1)
        expression.pop(i)
        i=0
    elif expression[i] == "/":
        expression[i] = int(expression[i-1]) / int(expression[i+1])
        expression.pop(i-1)
        expression.pop(i)
        i=0
    else:
        i+=1
print(expression, end = "\n\n\n")

#THIRD PRIORITY + and - (Add and Subtract)
i=0
while i < len(expression):
    if expression[i] == '+':
        expression[i] = int(expression[i-1]) + int(expression[i+1])
        expression.pop(i-1)
        expression.pop(i)
        i=0
    elif expression[i] == "-":
        expression[i] = int(expression[i-1]) - int(expression[i+1])
        expression.pop(i-1)
        expression.pop(i)
        i=0
    else:
        i+=1
print(expression, end = "\n\n\n")
