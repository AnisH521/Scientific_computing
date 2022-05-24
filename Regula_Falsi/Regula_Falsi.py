# importing necessary modules
import numpy as np

# defining the function f(x) = 0
def f(x):
    y = x*x*x + 2*x - 2
    return y

# function to calculate the root of the equation and to draw the the required table
def calculation():

    an = float(input('ENTER THE VALUE OF a0 : ')) # taking the initial interval from the user
    bn = float(input('ENTER THE VALUE OF b0 : ')) # taking the initial interval from the user
    n = int(input('ENTER THE NUMBER OF ITERATIONS : ')) # the number of iterations required 
    acc = int(input('ENTER THE ACCURACY LEVEL AFTER DECIMAL PLACES : ')) # accuracy level of decimal places 
    count = 0 # variable to stop the iteration

    print('\n\nOne root of f(x) = 0 lies between %f and %f \n Now we compute the successive approximations of the root as under\n\n' %(an, bn))
    print('-------------------------------------------------------------------------------------------------------')
    print('n         an                bn          f(an)         f(bn)         hn*           Xn+1**        f(Xn+1)')
    print('-------------------------------------------------------------------------------------------------------')

    while True:

        s = f(an) # for calculating f(an)
        g = f(bn) # for calculating f(bn)
        hn = (abs(s)*(bn - an))/(abs(s) + abs(g))# for calculating hn
        xm = an + hn # for calculating Xn+1
        k = f(xm) # for calculating f(Xn+1)

        print('%d       %f           %0.2f       %f      %f      %f      %f      %f' %(count, an, bn, s, g, hn, xm, k))

        # in (r+1)th iteration write Xr+1 in the column of an(+) if f(Xr+1) > 0 and
        # keep br fixed in the column bn(-). Otherwise write Xr+1 in the column of bn(-)
        # if f(Xr+1) < 0 and keep ar fixed in the column of an(+)

        if k > 0:
            if s >= 0:
                an = xm
            else:
                bn = xm
        elif k < 0:
            if s <= 0:
                an = xm
            else:
                bn = xm

        # incrementing count to keep the memory of number of iteration
        count = count + 1 

        # to stop the iteration when count becomes greater then n
        if count > n:
            print('\n\n*hn = |f(an)|*(bn - an)/|f(an)| + |f(bn)|')
            print('**Xn+1 = an + hn')
            print('\n\nThe Root is',round(xm,acc))
            break

# Defining main function
def main():
    print('\n\n***REGULA FALSI METHOD***\n\n')
    calculation()

# Using the special variable 
if __name__=="__main__":
    main()