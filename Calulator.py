
import time
operator = 1
x = 1
y = 1

    
    
def calculator():    
 print("Enter first number")
 x = input()

 print("Enter operator. 1 for multiply, 2 for divide , 3 for add")
 print("4 for subtract, 5 for exponet")
 operator = input()

 print("Enter second number")
 y = input()

 if str(operator) == "3":
    print("Anwser:")
    print(int(x) + int(y))

 if str(operator) == "2":
    print("Anwser:")
    print(int(x) / int(y))

 if str(operator) == "1":
    print("Anwser:")
    print(int(x) * int(y) )
   
 if str(operator) == "4":
   print("Anwser:")
   print(int(x) - int(y)) 
   
 if str(operator) == "5":
   print("Anwser:")
   print(int(x) ** int(y)) 
 time.sleep(2)  
  
 print("")  
 print("New Equation:")
 calculator()
calculator()   
   
   

    
    
    
    
    
