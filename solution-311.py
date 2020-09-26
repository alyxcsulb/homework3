# mpg calculator
# gal = gallons used
# mil = miles driven
# mpg = miles per gallon

SENTINEL = -1
result = []
while True: 
    gal = float(input("Enter the gallons used ( -1 to end ): "))
    if gal == SENTINEL : break
    mil = float(input("Enter the miles driven: "))
    mpg = mil / gal 
    print(f"The miles/gallon for this tank was {mpg: ,.6f}")
    result.append(mpg) 
    
print("The overall average miles/gallon was",sum(result)/len(result))
