# importing necessary module
import numpy as np

#first equation represented as a function f(x)
def f(x, y):
    expr = x**2 + x*y + y**2 - 7
    return expr

#second equation represented as a function g(x)
def g(x, y):
    expr = x**3 + y**3 - 9
    return expr

#fx calculation
def fx(x, y):
    expr = 2*x + y
    return expr

#fy calculation
def fy(x, y):
    expr = x + 2*y
    return expr

#gx calculation
def gx(x, y):
    expr = 3*x**2
    return expr

#gy calculation
def gy(x, y):
    expr = 3*y**2
    return expr

'''function to calculate the aprroximation of the root'''
def calculation():
    i = 0
    error = 100
    x0 = float(input('Enter the initial guess of x : \n'))
    y0 = float(input('Enter the initial guess of y : \n'))
    m = int(input('Enter the number of row of Xn+1 matrix : \n'))
    n = int(input('Enter the number of column of Xn+1 matrix : \n'))
    tol = float(input('Enter the tolerance level : \n')) 
        
    while np.all(abs(error) > tol):

        X0 = np.array([x0, y0], dtype = float).reshape(m, n)
        
        fnv = np.array([f(x0, y0), g(x0, y0)]).reshape(m, n)

        jac = np.array([[fx(x0, y0), fy(x0, y0)],
                        [gx(x0, y0), gy(x0, y0)]], dtype = float).reshape(2, m)
        inv_jac = np.linalg.inv(jac)

        Xn = X0 - inv_jac@fnv
        error = Xn - X0

        print('\ni=%d\n' %i)
        print('X%d=' %(i+1))
        print(Xn)
        print('-----------------\n')

        x0 = Xn[0]
        y0 = Xn[1]

        i = i + 1

    print('Thus the approximate root using Newton Raphson Method : \n')
    print('x = %f, y = %f\n' %(Xn[0], Xn[1]))
    print('The root is correct upto tolerance level of error entered by user')
    print('-----------------------------------------------------------------\n')

# Defining main function
def main():
    calculation()

# Using the special variable 
if __name__=="__main__":
    main()