# test
# gal = gallons used
# mil = miles driven
# mpg = miles per gallon

gal1 = float(input("Enter the gallons used (-1 to end): "))
mil1 = float(input("Enter the miles driven: "))
mpg1 = mil1 / gal1
print(f'The miles / gallon for this tank was {mpg1: ,.6f} \n')

gal2 = float(input("Enter the gallons used (-1 to end): "))
mil2 = float(input("Enter the miles driven: "))
mpg2 = mil2 / gal2
print(f'The miles / gallon for this tank was {mpg2: ,.6f} \n')

gal3 = float(input("Enter the gallons used (-1 to end): "))
mil3 = float(input("Enter the miles driven: "))
mpg3 = mil3 / gal3
print(f'The miles / gallon for this tank was {mpg3: ,.6f} \n')

overallmpg = (mil1 + mil2 + mil3) / (gal1 + gal2 + gal3)

gal4 = float(input("Enter the gallons used (-1 to end): "))
print(f'The overall average miles / gallom was {overallmpg: ,.6f}')


