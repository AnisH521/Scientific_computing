# importing necessary modules
import numpy as np

# defining the function f(x) = 0
def f(x):
    y = x + np.log(x) - 2
    return y

# defining the function for df(x)
def g(x):
    y = 1 + 1/x
    return y

# function to calculate the root of the equation and to draw the the required table
def calculation():
    
    an = float(input('ENTER THE VALUE OF a0 : ')) # taking the initial interval from the user
    bn = float(input('ENTER THE VALUE OF b0 : ')) # taking the initial interval from the user
    n = int(input('ENTER THE NUMBER OF ITERATIONS STARTING FROM 0 : ')) # the number of iterations required 
    acc = int(input('ENTER THE ACCURACY LEVEL AFTER DECIMAL PLACES : ')) # accuracy level of decimal places 
    count = 0 # variable to stop the iteration

    # to check if df(x) > 0 
    if g(an) > 0:
        print('\n\nOne root lies between %f and %f as df(x) > 0 for x belongs to [%f,%f]' %(an, bn, an, bn))

    print('\n\n----------------------------------------------------------')
    print('n        an          bn            Xn+1            f(Xn+1)')
    print('----------------------------------------------------------')

    while True:

        Xm = (an + bn)/2# for determining Xn+1
        fn1 = f(an)# for determining f(an)
        fn2 = f(bn)# for determining f(bn)
        fn3 = f(Xm)# for determining f(Xn+1)

        print('%d   %0.6f       %0.6f       %0.6f       %f' %(count, an, bn, Xm, fn3))

        #in r+1th iteration write Xr+1(=(ar+br)/2) in the column of an(+ve) if f(Xr+1) > 0
        # keeeping br fixed in the column of bn(-ve). Otherwise write Xr+1(=(ar+br)/2) in the 
        # column of bn(-ve) if f(Xr+1) < 0 keeping ar fixed in the coimn of an(+ve)
        if fn3 < 0:
            if fn1 < 0:
                an = Xm
            elif fn2 < 0:
                bn = Xm
        elif fn3 > 0:
            if fn1 > 0:
                an = Xm
            elif fn2 > 0:
                bn = Xm

        count = count + 1

        if count > n:
            print('\n\nThe root is ', round(Xm, acc))
            break

# Defining main function
def main():
    print('\n\n***BISECTION MOTHOD***\n\n')
    calculation()

# Using the special variable 
if __name__=="__main__":
    main()