# added is to print from largest to smallest

print("""ENTER FIVE NUMBERS AND I PRINT THEM IN DESCENDING ORDER :
      FIRST ENTER FIVE NUMBERS AND I IDENTIFY THE LARGEST
      NEXT ENTER FOUR AND I IDENTIFY THE SECOND THEN ENTER THREE
      THEN TWO AND FINALLY THE REMAINING ONE NUMBER
      EACH TIME EXCLUDE THE LAST NUMBERS THAT HAVE BEEN IDENTIFIED AS LARGE ALREADY
      """)

try:
    #First the user is going to enter five numbers,
    #They are compared against each other and the largest is printed
    
    
    num1 = int(input("\t\t\tEnter the first number : "))
    
    num2 = int(input("\t\t\tEnter the second number : "))
    
    num3 = int(input("\t\t\tEnter the third number : "))
    
    num4 = int(input("\t\t\tEnter the fourth number : "))
    
    num5 = int(input("\t\t\ttEnter the fourth number : "))
    
    #logic arrangement
    
    if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
        print("{} is the Largest".format(num1))
        
    if num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
        print("{} is the Largest".format(num2))
            
    if num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5:
        print("{} is the Largest".format(num3))
                
    if num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:
        print("{} is the Largest".format(num4))
                    
    if num5 > num1 and num5 > num2 and num5 > num3 and num5 > num4:
        print("{} is the Largest".format(num5))
        
    # since the largest number has been printed, now we ommit that number
    # and re-enter the remaining four values for comparison against @other
    # such that we get the second largest number
    
    numm1 = int(input("\t\t\tEnter the first number in any order of the remaining four values : "))
    
    numm2 = int(input("\t\t\tEnter the second number  : "))
    
    numm3 = int(input("\t\t\tEnter the third number : "))
    
    numm4 = int(input("\t\t\tEnter the fourth number : "))
    
    if numm1 > numm2 and numm1 > numm3 and numm1 > numm4:
        print("{} is the second largest".format(numm1))
        
    if numm2 > numm1 and numm2 > numm3 and numm2 > numm4:
        print("{} is the second largest".format(numm2))
        
    if numm3 > numm1 and numm3 > numm2 and numm3 > numm4:
        print("{} is the second largest".format(numm3))
        
    if numm4 > numm1 and numm3 > numm2 and numm4 > numm3:
        print("{} is the second largest".format(numm4))
        
    # now we have identified the first and second numbers
    # the user shud now ommit these 2 from the next input and only enter the remaining
    # 3 numbers for comparison
    
    nummm1 = int(input("\t\t\tEnter the other 3 numbers now omitting the to already identified\n\t\t\tEnter the first : "))
    
    nummm2 = int(input("\t\t\tEnter the second number : "))
                 
    nummm3 = int(input("\t\t\tEnter the third number : "))
    
    if nummm1 > nummm2 and nummm1 > nummm3:
        print("{} is the third largest".format(nummm1))
        
    if nummm2 > nummm1 and nummm2 > nummm3:
        print("{} is the third largest".format(nummm2))
        
    if nummm3 > nummm1 and nummm3 > nummm2:
        print("{} is the third largest".format(nummm3))
                 
                 
                    
except:
    print("Enter data again")