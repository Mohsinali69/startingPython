largest = -1
smallest = None
while True:
   
        
    num = input("Enter a number: ")
    if num == "done":
        break
    else :
         try:
              
              numbers=int(num)
         except:
              print("Invalid input")
              
         for number in num :
    
            if number > largest:
                largest=number
            elif number < smallest:
                smallest=number
            
    print(num)

print("Maximum is ", largest)
print("Minimum is ",smallest)
  