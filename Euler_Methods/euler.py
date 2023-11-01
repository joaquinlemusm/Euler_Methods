import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import pandas as pd

x, y = sp.symbols('x y')

def euler_method(x0, y0, h, xf, f):
    """
    Implementación del método de Euler
        :param float x0: Valor de x inicial
        :param float y0: Valor de y inicial
        :param float h: Step-size
        :param float xf: Valor de x final
        :param function f: Ecuación Diferencia Ordinaria
        :return: lista de resultados en x, lista de resultado en y, recuento del numero de iteraciones asociadas a cada valor en x, y
    """
    x = x0
    y = y0
    i = 1
    x_results = [x0]
    y_results = [y0]
    iteration = [i]

    while x < xf:
        y = y + h * f(x, y)
        x = x + h
        i += 1
        x_results.append(x)
        y_results.append(y)
        iteration.append(i)

    if x_results[-1] != xf:
        x_results.pop()
        y_results.pop()
        iteration.pop()

    return x_results, y_results, iteration


def improved_euler(x0, y0, h, xf, f):
    """
    Implementación del método de Euler Mejorado
        :param float x0: Valor de x inicial
        :param float y0: Valor de y inicial
        :param float h: Step-size
        :param float xf: Valor de x final
        :param function f: Ecuación Diferencia Ordinaria
        :return: lista de resultados en x, lista de resultados en y, recuento del numero de iteraciones asociadas a cada valor en x, y
    """
    x = x0
    y = y0
    i = 1
    x_results = [x0]
    y_results = [y0]
    iteration = [i]

    while x < xf:
        implicit_euler = y + h * f(x, y)
        y = y + h * (f(x,y) + f(x+h,implicit_euler))/2
        x += h
        i += 1
        x_results.append(x)
        y_results.append(y)
        iteration.append(i)
    
    if x_results[-1] != xf:
        x_results.pop()
        y_results.pop()
        iteration.pop()

    return x_results, y_results, iteration


def graph_methods(x, y_euler, y_improved):
    """
    Graficación de los métodos de Euler
        :param list x: Valores de x asociados a la evaluación de funciones
        :param list y_euler: Valores de y asociados a la implementación del método de Euler
        :param list y_improved: Valores de y asociados a la implementación del método de Euler Mejoradoes
    """
    plt.plot(x, y_euler, label='Euler')
    plt.plot(x, y_improved, label='Euler Mejorado')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Solución de la Ecuación Diferencial')
    plt.grid(True)
    plt.legend()
    plt.show()


def data_table(i, x, y_euler, y_improved):
    """
    Tabulación de los datos obtenidos a partir de la aplicación de los métodos
        :param list i: Iteraciones realizados durante la ejecución de los algoritmos
        :param list x: Valores de x asociados a la evaluación de funciones
        :param list y_euler: Valores de y asociados a la implementación del método de Euler
        :param list y_improved: Valores de y asociados a la implementación del método de Euler Mejoradoes
    """

    df = pd.DataFrame(zip(i, x, y_euler, y_improved), columns=["Iteracion", "x", "Euler", "Euler Mejorado"])
    df = df.round(4)
    print(df.to_string(index=False))


def main():
    # Obtención de los datos proporcionados por el usuario.
    edo_text = input("Introduce la ecuación diferencial de la forma dy/dx = f(x, y): ")
    x0 = float(input("Ingrese el valor inicial de x: "))
    y0 = float(input("Ingrese el valor inicial de y: "))
    xf = float(input("Ingrese el valor final de x: "))
    h = float(input("Ingrese el step-size: "))

    # Convierte la EDO en texto plano en una función
    edo_expr = sp.sympify(edo_text)
    f = sp.lambdify((x, y), edo_expr, 'numpy')

    # Uso de los métodos de Euler
    x_euler, y_euler, iterations = euler_method(x0, y0, h, xf, f)
    x_improved, y_improved, iterations = improved_euler(x0, y0, h, xf, f)

    # Visualización gráfica de los métodos numéricos
    data_table(iterations, x_euler, y_euler, y_improved)
    graph_methods(x_euler, y_euler, y_improved)

if __name__ == '__main__':
    main()
