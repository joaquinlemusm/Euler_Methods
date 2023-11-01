import euler
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import pandas as pd
import math

x, y = sp.symbols('x y')

def f1(x, y):
    """
    Representación de la EDO y' = e^2y
        :param list x: Valores de x asociados a la EDO
        :param list y: Valores de y asociados a la EDO
    """
    return np.exp(2*y)

def f2(x, y):
    """
    Representación de la EDO y' = (x+y-2)^2
        :param list x: Valores de x asociados a la EDO
        :param list y: Valores de y asociados a la EDO
    """
    return (x+y-2)**2

def f3(x, y):
    """
    Representación de la EDO y' = 0.9y - 1.8y^2
        :param list x: Valores de x asociados a la EDO
        :param list y: Valores de y asociados a la EDO
    """
    return (0.9*y) - (1.8*y**2)

def exact_f1(x):
    """
    Representación de la solución exacta de la EDO y' = e^2y
        :param list x: Valores de x asociados a la exacta
    """
    return -1/2*np.log(2*(0.5-x))

def exact_f2(x):
    """
    Representación de la solución exacta de la EDO y' = (x+y-2)^2
        :param list x: Valores de x asociados a la exacta
    """
    return math.tan(x) + 2 - x

def exact_f3(x):
    """
    Representación de la solución exacta de la EDO y' = 0.9y - 1.8y^2
        :param list x: Valores de x asociados a la exacta
    """
    c = (1/0.47)-2
    return (np.exp(0.9*x)/(c+2*np.exp(0.9*x)))

def graph_specific_functions(x, y_euler, y_exact):
    """
    Graficación de los métodos de Euler en conjunto a la solución exacta
        :param list x: Valores de x asociados a la evaluación de funciones
        :param list y_euler: Valores de y asociados a la implementación del método de Euler
        :param list y_exact: Valores de y asociados a la solución exacta
    """
    plt.plot(x, y_euler, label='Euler')
    plt.plot(x, y_exact, label='Exacta')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Solución de la Ecuación Diferencial')
    plt.grid(True)
    plt.legend()
    plt.show()

def specific_data_table(i, x, y_euler, y_exact, absolute, relative):
    """
    Tabulación de los datos obtenidos a partir de la aplicación del método de Euler y la solución exacta en conjunto a los errores absolutos y relativos
        :param list i: Iteraciones realizados durante la ejecución de los algoritmos
        :param list x: Valores de x asociados a la evaluación de funciones
        :param list y_euler: Valores de y asociados a la implementación del método de Euler
        :param list y_exact: Valores de y asociados a la solución exacta
        :param list absolute: Error absoluto respecto a los valores de euler y la exacta
        :param list relative: Error relativo respecto a los valores de euler y la exacta
    """
    df = pd.DataFrame(zip(i, x, y_euler, y_exact, absolute, relative), columns=["Iteracion", 
                                                                                "x", 
                                                                                "Euler", 
                                                                                "Exacto", 
                                                                                "Error absoluto", 
                                                                                "Error relativo"])
    df = df.round(4)
    print(df.to_string(index=False))

def compare_values(euler, exact):
    """
    Comparación de los valores finales entre un método Euler y los valores exactos
        :param list y_euler: Valores de y asociados a la implementación del método de Euler
        :param list y_exact: Valores de y asociados a la solución exacta
    """
    y_euler = round(euler[-1],4)
    y_exact = round(exact[-1],4)
    error = round(porcentual_error(y_euler, y_exact),4)

    print(f"Valor aproximado: {y_euler}\nValor exacto: {y_exact}")
    print(f"Error porcentual: {error}%")

def relative_error(euler, exact):
    """
    Calculo del error relativo entre un método de Euler y los valores exactos.
        :param list y_euler: Valores de y asociados a la implementación del método de Euler
        :param list y_exact: Valores de y asociados a la solución exacta
    """
    error = []
    for i in range(len(euler)):
        if exact[i] == euler[i]:
            error.append(0)
            continue
        error.append(abs(exact[i]-euler[i])/abs(exact[i]))
    return error

def absolute_error(euler, exact):
    """
    Calculo del error absoluto entre un método de Euler y los valores exactos.
        :param list y_euler: Valores de y asociados a la implementación del método de Euler
        :param list y_exact: Valores de y asociados a la solución exacta
    """
    error = []
    for i in range(len(euler)):
        error.append(abs(exact[i]-euler[i]))
    return error

def porcentual_error(euler, exact):
    """
    Calculo del error porcentual entre un método de Euler y los valores exactos.
        :param list y_euler: Valores de y asociados a la implementación del método de Euler
        :param list y_exact: Valores de y asociados a la solución exacta
    """
    return abs((euler-exact)/exact)*100

def specific_functions(x0, y0, h, xf, function_number):
    """
    Validación para la aplicación de determinano método de Euler en conjunto al cálculo del error absoluto y relativo
        :param float x0: Valor de x inicial
        :param float y0: Valor de y inicial
        :param float h: Step-size
        :param float xf: Valor de x final
        :param int function_number: Parametro con la finalidad de diferenciar la ecuacion diferencial a resolver
        :return: lista de resultados en x, lista de resultados en y de Euler, lista de resultados en y Exacta, recuento del numero de iteraciones asociadas a cada valor en x, y, lista de error relativo, lista de error absoluto 
    """
    if function_number == 1:
        x_euler, y_euler, iterations = euler.euler_method(x0, y0, h, xf, f1)
        y_exact = [exact_f1(x) for x in x_euler]
    elif function_number == 2:
        x_euler, y_euler, iterations = euler.improved_euler(x0, y0, h, xf, f2)
        y_exact = [exact_f2(x) for x in x_euler]  
    elif function_number == 3:
        x_euler, y_euler, iterations = euler.improved_euler(x0, y0, h, xf, f3)
        y_exact = [exact_f3(x) for x in x_euler]   

    relative = relative_error(y_euler, y_exact)
    absolute = absolute_error(y_euler, y_exact)

    return iterations, x_euler, y_euler, y_exact, relative, absolute

def validate_expression(edo_text):
    """
    Validación de expresiones que concuerden con las ecuaciones diferenciales ordinarias dadas.
        :param string edo_text: Ecuación diferencial ordinaria en texto
        :return: boolean 
    """
    if edo_text == "exp(2*y)" or edo_text == "(x+y-2)**2" or edo_text == "0.9*y - 1.8*y**2":
        return True
    return False

def practice_guide(edo_text, x0, y0, h, xf):
    """
    Ejecución de la guía práctica
        :param string edo_text: Ecuación diferencial ordinaria en texto
        :param float x0: Valor de x inicial
        :param float y0: Valor de y inicial
        :param float h: Step-size
        :param float xf: Valor de x final
    """
    if edo_text == "exp(2*y)":
        specific_functions(x0, y0, h, xf, 1)
    elif edo_text == "(x+y-2)**2":
        specific_functions(x0, y0, h, xf, 2)
    elif edo_text == "0.9*y - 1.8*y**2":
        specific_functions(x0, y0, h, xf, 3)