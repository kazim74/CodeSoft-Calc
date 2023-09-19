
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def div(x, y):
    if y == 0:
        return "Not possible"
    return x / y
    
def mul(x, y):
    return x * y


try:
    n1 = float(input("Enter 1st number: "))
    n2 = float(input("Enter 2nd number: "))
except ValueError:
    print("Invalid")
    exit()


print("Choose operation:\n1) Add\n2) Subtract\n3) Multiply\n4) Divide")


while True:
    try:
        choice = int(input("Enter the operation 1,2,3,4: "))
        if choice in [1, 2, 3, 4]:
            break 
        else:
            print("Choose 1, 2, 3, or 4")
    except ValueError:
        print("Invalid. Choose the integers mentioned above")

if choice == 1:
    result = add(n1, n2)
    
    
elif choice == 2:
    result = sub(n1, n2)
    
    
elif choice == 3:
    result = mul(n1, n2)
    
    
elif choice == 4:
    result = div(n1, n2)
    
    
else:
    print("Invalid choice. Please choose 1,2,3, or 4")
    exit()

print(f"The answer is: {result}")


