print("A = Celsius to Fahrenheit")
print("B = Fahrenheit to Celsius")

option = input("Insert A or B: ")

if option == "A":
    c = float(input("Insert Celsius: "))   
    f = (c * 9/5) + 32                     
    print("Fahrenheit:", f)

elif option == "B":
    f = float(input("Insert Fahrenheit: ")) 
    c = (f - 32) * 5/9
    print("Celsius:", c)

else:
    print("Error: Insert only A or B")


