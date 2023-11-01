import customtkinter as ctk
import euler
import practice_guide
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import tkinter as tk
from tkinter import ttk

x, y = sp.symbols('x y')

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.geometry("1000x1000")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Métodos de Euler")
label.pack(pady=55, padx=10)

# Cambiar la fuente y el tamaño del título
label.configure(font=("Helvetica", 35))

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Crear un frame para los textBox
entry_frame = ctk.CTkFrame(master=frame)
entry_frame.pack(side=tk.LEFT, fill="both", expand=True)

# Creacion de los textBox
entry1 = ctk.CTkEntry(master=entry_frame, placeholder_text="Ecuación diferencial:")
entry1.pack(pady=12, padx=10, anchor="center")

entry2 = ctk.CTkEntry(master=entry_frame, placeholder_text="Valor inicial de x:")
entry2.pack(pady=12, padx=10, anchor="center")

entry3 = ctk.CTkEntry(master=entry_frame, placeholder_text="Valor inicial de y:")
entry3.pack(pady=12, padx=10, anchor="center")

entry4 = ctk.CTkEntry(master=entry_frame, placeholder_text="Valor final de x:")
entry4.pack(pady=12, padx=10, anchor="center")

entry5 = ctk.CTkEntry(master=entry_frame, placeholder_text="Step-size (h): ")
entry5.pack(pady=12, padx=10, anchor="center")

# Crear un frame para la tabla y la gráfica
graph_frame = ctk.CTkFrame(master=frame)
graph_frame.pack(side=tk.RIGHT, fill="both", expand=True)


# Crear un marco para la tabla de datos
data_frame = ctk.CTkFrame(master=root)
data_frame.pack(pady=20, padx=60, fill="both", expand=True)

# Creación del frame para las tablas
tree_frame = ctk.CTkFrame(data_frame)
tree_frame.pack(side=tk.LEFT, padx=5, fill="both", expand=True)
tree1_frame = ctk.CTkFrame(data_frame)
tree1_frame.pack(side=tk.LEFT, padx=5, fill="both", expand=True)

# Creación de la tabla de datos
tree = ttk.Treeview(tree_frame, columns=("Iteration", "x", "y (Euler)", "y (Euler Mejorado)"))
tree1 = ttk.Treeview(tree1_frame, columns=("Iteration", "x", "y (Euler)", "y (Exacta)", "Error absoluto", "Error relativo"))

# Configuración de las columnas de la tabla
for col in ("Iteration", "x", "y (Euler)", "y (Euler Mejorado)"):
    tree.heading(col, text=col)
    tree.column(col, width=100)

for col in ("Iteration", "x", "y (Euler)", "y (Exacta)", "Error absoluto", "Error relativo"):
    tree1.heading(col, text=col)
    tree1.column(col, width=100)  

tree.pack(fill="both", expand=True)
tree1.pack(fill="both", expand=True)

# Solucionar Ecuaciones Diferencias Ordinarias
def solve_differential_equation():
    edo_text = entry1.get()
    x0 = float(entry2.get())
    y0 = float(entry3.get())
    xf = float(entry4.get())
    h = float(entry5.get())

    if edo_text == "exp(2*y)" or edo_text == "(x+y-2)**2" or edo_text == "0.9*y - 1.8*y**2":
        if edo_text == "exp(2*y)":
            iterations, x_euler, y_euler, y_exact, relative, absolute = practice_guide.specific_functions(x0, y0, h, xf, 1)
 
            x_euler = [round(val, 4) for val in x_euler]
            y_euler = [round(val, 4) for val in y_euler]
            y_exact = [round(val, 4) for val in y_exact]
            relative = [round(val, 4) for val in relative]
            absolute = [round(val, 4) for val in absolute]
            
            data = {"Iteration": iterations, 
                    "x": x_euler, 
                    "y (Euler)": y_euler, 
                    "y (Exacta)": y_exact,
                    "Error absoluto": absolute, 
                    "Error relativo": relative
                    }
            df = pd.DataFrame(data)   
            # Limpiar la tabla antes de agregar una nueva tabla
            for item in tree1.get_children():
                tree1.delete(item)
            # Agregar los datos a la tabla
            for index, row in df.iterrows():
                tree1.insert("", "end", values=(row["Iteration"], row["x"], row["y (Euler)"], row["y (Exacta)"], row["Error absoluto"], row["Error relativo"]))
            draw_exact_graphs(x_euler, y_euler, y_exact)
        elif edo_text == "(x+y-2)**2":
            iterations, x_euler, y_euler, y_exact, relative, absolute = practice_guide.specific_functions(x0, y0, h, xf, 2)
 
            x_euler = [round(val, 4) for val in x_euler]
            y_euler = [round(val, 4) for val in y_euler]
            y_exact = [round(val, 4) for val in y_exact]
            relative = [round(val, 4) for val in relative]
            absolute = [round(val, 4) for val in absolute]
            
            data = {"Iteration": iterations, 
                    "x": x_euler, 
                    "y (Euler)": y_euler, 
                    "y (Exacta)": y_exact,
                    "Error absoluto": absolute, 
                    "Error relativo": relative
                    }
            df = pd.DataFrame(data)   
            # Limpiar la tabla antes de agregar una nueva tabla
            for item in tree1.get_children():
                tree1.delete(item)
            # Agregar los datos a la tabla
            for index, row in df.iterrows():
                tree1.insert("", "end", values=(row["Iteration"], row["x"], row["y (Euler)"], row["y (Exacta)"], row["Error absoluto"], row["Error relativo"]))
            draw_exact_graphs(x_euler, y_euler, y_exact)
        elif edo_text == "0.9*y - 1.8*y**2":
            iterations, x_euler, y_euler, y_exact, relative, absolute = practice_guide.specific_functions(x0, y0, h, xf, 3)
            
            x_euler = [round(val, 4) for val in x_euler]
            y_euler = [round(val, 4) for val in y_euler]
            y_exact = [round(val, 4) for val in y_exact]
            relative = [round(val, 4) for val in relative]
            absolute = [round(val, 4) for val in absolute]
            
            data = {"Iteration": iterations, 
                    "x": x_euler, 
                    "y (Euler)": y_euler, 
                    "y (Exacta)": y_exact,
                    "Error absoluto": absolute, 
                    "Error relativo": relative
                    }
            df = pd.DataFrame(data)   
            # Limpiar la tabla antes de agregar una nueva tabla
            for item in tree1.get_children():
                tree1.delete(item)
            # Agregar los datos a la tabla
            for index, row in df.iterrows():
                tree1.insert("", "end", values=(row["Iteration"], row["x"], row["y (Euler)"], row["y (Exacta)"], row["Error absoluto"], row["Error relativo"]))
            draw_exact_graphs(x_euler, y_euler, y_exact)
    else:
        edo_expr = sp.sympify(edo_text)
        f = sp.lambdify((x, y), edo_expr, 'numpy')

        x_euler, y_euler, iterations = euler.euler_method(x0, y0, h, xf, f)
        x_improved, y_improved, iterations = euler.improved_euler(x0, y0, h, xf, f)

        x_euler = [round(val, 4) for val in x_euler]
        y_euler = [round(val, 4) for val in y_euler]
        x_improved = [round(val, 4) for val in x_improved]
        y_improved = [round(val, 4) for val in y_improved]

        # Crear una tabla de datos para mostrar los resultados
        data = {"Iteration": iterations, "x": x_euler, "y (Euler)": y_euler, "y (Improved Euler)": y_improved}
        df = pd.DataFrame(data)

        # Limpiar la tabla antes de agregar una nueva tabla
        for item in tree.get_children():
            tree.delete(item)

        # Agregar los datos a la tabla
        for index, row in df.iterrows():
            tree.insert("", "end", values=(row["Iteration"], row["x"], row["y (Euler)"], row["y (Improved Euler)"]))
        
        draw_graphs(x_euler, y_euler, y_improved)


def draw_exact_graphs(x_euler, y_euler, y_exacta):
    # Crear una figura para las gráficas
    fig, ax = plt.subplots(figsize=(2, 2))
    ax.plot(x_euler, y_euler, label="Euler")
    ax.plot(x_euler, y_exacta, label="Exacta")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()

    # Crear el lienzo para la figura
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

def draw_graphs(x_euler, y_euler, y_improved):
    # Crear una figura para las gráficas
    fig, ax = plt.subplots(figsize=(2, 2))
    ax.plot(x_euler, y_euler, label="Euler")
    ax.plot(x_euler, y_improved, label="Euler Mejorado")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()

    # Crear el lienzo para la figura
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

def clear():
    entry1.delete(0, "end")
    entry2.delete(0, "end")
    entry3.delete(0, "end")
    entry4.delete(0, "end")
    entry5.delete(0, "end")
    
    # Borrar la tabla
    for item in tree.get_children():
        tree.delete(item)
        
    for item in tree1.get_children():
        tree1.delete(item)
    clear_graph()

def clear_graph():
    # Limpiar la figura que almacena la gráfica
    for widget in graph_frame.winfo_children():
        widget.destroy()

# Configuración de los botones Solve y Clear
button = ctk.CTkButton(master=frame, text="Solve", command=solve_differential_equation)
button.pack(pady=12, padx=10, anchor="center")

button = ctk.CTkButton(master=frame, text="Clear", command=clear)
button.pack(pady=12, padx=10, anchor="center")  

# Ejecución de la interfaz gráfica
root.mainloop()