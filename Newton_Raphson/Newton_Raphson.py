#importing necessary modules
import numpy as np

#defining the function f(x) = 0
def f(x):
    y = x + np.log(x) - 2
    return y

#defining the derivative of the function f'(x) = 0 as g(x) = 0
def g(x):
    y = 1 + 1/x
    return y

#function to calculate root of the equation and print its values in a table
def calculation():
    initial_guess = float(input('ENTER THE INITIAL GUESS : '))
    user_step = int(input('ENTER THE NUMBER OF STEPS REQUIRED : '))
    acc = int(input('ENTER THE ACCURACY LEVEL AFTER DECIMAL PLACES : '))

    print('\n\nTaking X0 = %f, the successive approximations of the root are computed in the following table--' %(initial_guess))

    print('\n\n----------------------------------------------------------------------------')
    print('\nITERAION    Xn        f(Xn)      df(Xn)  hn = -f(Xn)/g(Xn)    Xn+1 = Xn + hn')
    print('\n----------------------------------------------------------------------------')

    iteration = 0
    Xn = initial_guess

    while True:
        
        FXn = f(Xn)
        GXn = g(Xn)
        hn = -(f(Xn)/g(Xn))
        Xn2 = Xn + hn

        print('%d        %f   %0.7f    %0.4f    %f           %0.8f' %(iteration, Xn, FXn, GXn, hn, Xn2))
        iteration = iteration + 1
        Xn = Xn2
        if (iteration > user_step):
            print('\n\nThe Root is',round(Xn,acc))
            break

# Defining main function
def main():
    print('\n\n***NEWTON RAPHSON METHOD***\n\n')
    calculation()

# Using the special variable 
if __name__=="__main__":
    main()