Arpita's  Calculator Project

def add(a, b): return a + b
def minus(a, b): return a - b
def multiply(a, b): return a * b
def  divide(a, b):
return a / b if b != 0 else "Error: Zero se divide nahi kar sakte!"

print("--- Arpita's Python Calculator ---")

while True:
print("\nKya karna chahenge? (1:Add, 2:Minus, 3:Multiply, 4:Divide, 5:Bas bahut hua!)")
option = input("Choose your option: ")

if option == '5':  
    print("Phir milenge! Bye.")  
    break  

try:  
    val1 = float(input("Pehla number batao: "))  
    val2 = float(input("Dusra number batao: "))  
      
    if option == '1': print(f"Result: {add(val1, val2)}")  
    elif option == '2': print(f"Result: {minus(val1, val2)}")  
    elif option == '3': print(f"Result: {multiply(val1, val2)}")  
    elif option == '4': print(f"Result: {divide(val1, val2)}")  
    else: print("Arey! Sahi option chuno.")  
      
except ValueError:  
    print("Number daalna tha, kya kar rahe ho?")
