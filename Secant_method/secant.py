# imporing required modules
import numpy as np

# defining the function f(x) = 0
def f(x):
    y = np.cos(x) - x*np.exp(x)
    return y

# function to calculate the root and printing the values in table 
def calculation():

    X0 = float(input('ENTER THE VALUE OF X0 : ')) # taking the initial interval from the user
    X1 = float(input('ENTER THE VALUE OF X1 : ')) # taking the initial interval from the user
    k = int(input('ENTER THE NUMBER OF ITERATIONS : ')) # the number of iterations required 
    acc = int(input('ENTER THE ACCURACY LEVEL AFTER DECIMAL PLACES : ')) # accuracy level of decimal places 
    count = 1 # variable to stop the iteration
    i = 2

    print('\n\nCalculation of the root by iteration is given in following table')

    print('\n\n------------------------------------')
    print('k              Xk+1          f(Xk+1)')
    print('------------------------------------')

    while True:
        
        Xn = X1 - ((X1 - X0)/(f(X1) - f(X0)))*f(X1)# calculating Xk+1
        X0 = X1# setting up Xk-1
        X1 = Xn# setting up Xk
        
        print('%d       (X%d=)%0.6f       %0.6f' %(count, i, Xn, f(Xn)))

        count = count + 1
        i = i + 1

        if count > k:
            print('\n\nThe root is ', round(Xn, acc))
            break

# Defining main function
def main():
    print('\n\n***SECANT METHOD***\n\n')
    calculation()

# Using the special variable 
if __name__=="__main__":
    main()