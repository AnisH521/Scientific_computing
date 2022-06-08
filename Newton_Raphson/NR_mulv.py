# importing necessary modules
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# first equation represented as a function f(x,y)
def f(x0, y0, expr1):
    x, y = sym.symbols('x y')
    expr1 = eval(expr1, {"x": x0, "y": y0})
    return expr1
# second equation represented as a function g(x,y)
def g(x0, y0, expr2):
    x, y = sym.symbols('x y')
    expr2 = eval(expr2, {"x": x0, "y": y0})
    return expr2

# fx calculation
def fx(x0, y0, exprf):
    x, y = sym.symbols('x y')
    exprf = sym.diff(exprf, x).doit()
    diff = str(exprf)
    diff = eval(diff, {"x": x0, "y": y0})
    return diff

# fy calculation
def fy(x0, y0, exprf):
    x, y = sym.symbols('x y')
    exprf = sym.diff(exprf, y).doit()
    diff = str(exprf)
    diff = eval(diff, {"x": x0, "y": y0})
    return diff

# gx calculation
def gx(x0, y0, exprg):
    x, y = sym.symbols('x y')
    exprg = sym.diff(exprg, x).doit()
    diff = str(exprg)
    diff = eval(diff, {"x": x0, "y": y0})
    return diff

# gy calculation
def gy(x0, y0, exprg):
    x, y = sym.symbols('x y')
    exprg = sym.diff(exprg, y).doit()
    diff = str(exprg)
    diff = eval(diff, {"x": x0, "y": y0})
    return diff

'''function to calculate the aprroximation of the root'''
def calculation():
    i = 0
    error = 100
    expr1 = input('Enter equation 1 : ')
    expr2 = input('Enter equation 2 : ')
    x0 = float(input('Enter the initial guess of x : \n'))
    y0 = float(input('Enter the initial guess of y : \n'))
    m = int(input('Enter the number of row of Xn+1 matrix : \n'))
    n = int(input('Enter the number of column of Xn+1 matrix : \n'))
    tol = float(input('Enter the tolerance level : \n'))

    exprf = expr1
    exprg = expr2
    x_axis = np.array([])
    y_axis = np.array([])
 
        
    while np.all(abs(error) > tol):

        X0 = np.array([x0, y0], dtype = float).reshape(m, n)
        
        fnv = np.array([f(x0, y0, expr1), g(x0, y0, expr2)]).reshape(m, n)

        jac = np.array([[fx(x0, y0, exprf), fy(x0, y0, exprf)],
                        [gx(x0, y0, exprg), gy(x0, y0, exprg)]], dtype = float).reshape(2, m)
        inv_jac = np.linalg.inv(jac)

        Xn = X0 - inv_jac@fnv
        error = Xn - X0

        print('\ni=%d\n' %i)
        print(f"X{i+1} = {Xn}")
        print('-----------------\n')

        x0 = Xn[0]
        y0 = Xn[1]

        x_axis = np.append(x_axis, x0)
        y_axis = np.append(y_axis, y0)

        i = i + 1

    font1 = {'family':'monospace','color':'maroon','size':20}
    font2 = {'family':'monospace','color':'maroon','size':20}
    font3 = {'family':'sans-serif','color':'indianred','size':25}

    plt.plot(x_axis, y_axis, marker = '*')
    plt.title('Plot of Newton Raphson Multivariate', fontdict = font3)
    plt.xlabel("X", fontdict = font1)
    plt.ylabel("Y", fontdict = font2)
    plt.show()

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