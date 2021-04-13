import pandas as pd
import matplotlib.pyplot as plt

compras = pd.read_csv(r"C:\Users\LENOVO\PycharmProjects\Practica Pandas - Matplotlib\compra+curso.csv", sep = ";")
print(compras.head())

#Se usara información de las columnas compras del curso y calificaciones
grafico = compras[["Compras_del_curso", "calificaciones"]]
print(grafico.describe())

plt.style.use("seaborn-whitegrid")

fig, ax = plt.subplots(figsize = (15,8))

ax.plot(grafico.Compras_del_curso, grafico.calificaciones, marker = "o", linestyle = "", markersize = 9, color = "red", markeredgecolor = "blue", markeredgewidth = 1.5)

ax.set_xlabel("Compras del curso", fontname='Comic Sans MS', fontsize = 20)
ax.set_ylabel("Calificacion del curso", fontname = 'Comic Sans MS', fontsize = 20)
ax.set_title("Ventas y Calificaciones", fontname ="fantasy", fontsize = 25, va = "bottom")

plt.show()