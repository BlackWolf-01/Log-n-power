#Program to compute X^Y without using maths function
def Computepower(x,y):
    result=1
    while(y>0):
        #If y is even 
        if(y%2==0):
            x=x*x
            y>>=1
        else:
            result=result*x
            y=y-1
    return result
x=int(input('Enter the value of x'))            
y=int(input('Enter the value of y')) 
print('Total ',(Computepower(x,y)))