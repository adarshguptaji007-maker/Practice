# simple addition 
a = 67 ;
b = 34 ;
print(a + b) ;

print(67 + 34);
print(67 + 89);


#function Initialize to add numbers 
def sumNumber(a,b) :
   
#    Function definition
   return (a+b)
# function calling 
c=sumNumber(24,25)
print(c)

# Simple Interest = P * r * T/100 p = PRINCIPAL | r = RATE | T = Time

P = 5000
R = 8
T = 2
SI=(P*R*T)/100
print ("SI = ",SI)


# USING FUNCTION
def calSI(P,R,T):
   return ((P*R*T)/100)

# CALL FUNCTION CALSI
print(calSI(5000,8,2))


# convert kg to gm simple
# function initialization 

def kgtogm(kg) :
   return (kg*1000)

# function calling
print (kgtogm(4) , "g")



