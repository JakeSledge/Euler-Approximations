import matplotlib.pyplot as plt
import numpy as np
from math import ceil
import sympy as sy


def Euler_approximation(formula, x, y, h_step, x_max):
    # x any y lists to plot from
    x_list = []
    y_list = []
    euler_list = Euler_approximation_recurse(formula,x,y,h_step,x_max,x_list,y_list)
    x_list = euler_list[1]
    y_list = euler_list[2]
    plt.plot(x_list, y_list)
    plt.xlabel('x')
    plt.ylabel('y')
    # solution of the given formula
    formula_of_diff = sol
    ran = np.linspace(x_list[0],x_list[-1], 35)
    graph(formula_of_diff, ran)
    plt.show()
    return euler_list[0]


def Euler_approximation_recurse(formula, x, y, h_step, x_max, x_list, y_list):
    # add x and y to the list to plot
    x_list.append(x)
    y_list.append(y)
    if x >= x_max:
        # end if the x has reached the x_max
        return [y, x_list, y_list]
    # calculate the derivative value
    F = myformula(x=x, y=y, formula=formula)
    x_next = x + h_step
    # round
    x_next = ceil(x_next*10000)/10000
    y_next = y + h_step*F
    return Euler_approximation_recurse(formula, x_next, y_next, h_step, x_max, x_list, y_list)


def myformula(formula, **kwargs):
    expr = sy.sympify(formula)
    return expr.evalf(subs=kwargs)


def graph(formula_of_diff_sol, x_range):
    x = np.array(x_range)
    y = eval(formula_of_diff_sol)
    plt.plot(x, y)


formula = input("What is the differetial equation? ")
global sol
sol = input("What is its solution: ")
x = float(input("x naught: "))
y = float(input("y nought: "))
new_y = Euler_approximation(formula, x, y, 1, 5)
new_y = Euler_approximation(formula, x, y, .1, 5)
new_y = Euler_approximation(formula, x, y, .01, 5)
new_y = Euler_approximation(formula, x, y, .001, 5)