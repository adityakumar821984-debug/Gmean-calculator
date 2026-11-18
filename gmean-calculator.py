# A simple program to calculate the gmean using def
# Authored by Aditya
print("***********GMEAN CALCULATOR**************")
print("\n")
# FOR CALCULATING THE GMEAN:
def Calculate_gmean(a, b):
    if a<0 or b<0 :
        print("Calculating by 0 is not approved")
    else:
        mean = (a*b)**0.5
        print("geometrical mean of",a,"and",b,"is",mean)


# FOR CHEKING THE GREATER NUMBER:
def is_greater(a, b):
    if (a > b):
        print( a,"is bigger than",b)
   
    elif (a < b):
        print(b, "is greater than",a)
   
      

# FOR CHEKING THE SMALLER NUMBER
def Is_lesser(a, b):
    if(a<b):
        print(a,"is smaller than ",b)
    elif(a>b):
        print(b,"is smaller than",a)
    else:
        print(a,"=",b)
i = 'y'

while i.lower() == 'y':
   

   # FOR TAKING USER INPUT
   a = int(input("Enter the first number:"))
   b= int(input("Enter the second number:"))
   print("\n")

   # FOR SHOWING THE OUTPUT
   Calculate_gmean(a, b)
   print("\n")
   is_greater(a, b)
   print("\n") 
   Is_lesser(a, b)
   print("\n") 
   i = input("want another calculation, (y/n)")