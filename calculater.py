while True:

     print("---calculator---")
     a=int(input("enter the first number:"))
     b=int(input("enter the secong number:"))
     operation=input("enter the operation:")
     if  operation=="+":
         print("sum =",a+b)

     elif operation=="-":
         print("difference=",a-b)

     elif operation=="*":
         print("multiplication=",a*b)

     elif operation=="/":
         if b!=0:
           print("division=",a/b)
         else:
             print ("can't divided by zero")

     elif operation=="//":
         if b != 0:
           print("floor division=",a//b)
         else:
            print ("can't divided by zero")
        
     elif operation=="%":
         if b != 0:
           print("Remainder=",a%b)
         else:
            print ("can't divided by zero")

     elif operation=="**":
         print("exponencial=",a**b)

     else:
         print("Invalid operation")
     choice = input("\nDo you want to perform another calculation? (yes/no): ")

     if choice.lower() != "yes":
        print("Calculator closed. Thank you!")
        break

