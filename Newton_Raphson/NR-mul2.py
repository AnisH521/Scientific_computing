# importing necessary modules
import numpy as np
import sympy as sym

# first equation represented as a function f(x,y)
f = lambda x, y : x**2 + x*y + y**2 - 7
# second equation represented as a function g(x,y)
g = lambda x, y : x**3 + y**3 - 9

# fx calculation
def fx(x0, y0):
    x, y = sym.symbols('x y')
    expr = x**2 + x*y + y**2 - 7
    diff = sym.diff(expr, x).doit()
    diff = str(diff)
    diff = eval(diff, {"x": x0, "y": y0})
    return diff

# fy calculation
def fy(x0, y0):
    x, y = sym.symbols('x y')
    expr = x**2 + x*y + y**2 - 7
    diff = sym.diff(expr, y).doit()
    diff = str(diff)
    diff = eval(diff, {"x": x0, "y": y0})
    return diff

# gx calculation
def gx(x0, y0):
    x, y = sym.symbols('x y')
    expr = x**3 + y**3 - 9
    diff = sym.diff(expr, x).doit()
    diff = str(diff)
    diff = eval(diff, {"x": x0, "y": y0})
    return diff

# gy calculation
def gy(x0, y0):
    x, y = sym.symbols('x y')
    expr = x**3 + y**3 - 9
    diff = sym.diff(expr, y).doit()
    diff = str(diff)
    diff = eval(diff, {"x": x0, "y": y0})
    return diff

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
        print(f"X{i+1} = {Xn}")
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