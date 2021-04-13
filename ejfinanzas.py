import pandas as pd
import matplotlib.pyplot as plt

fin = pd.read_csv(r"C:\Users\LENOVO\PycharmProjects\Practica Pandas - Matplotlib\finanzas.csv")
#print(fin)
columnas = fin.columns.values
print(columnas)

#Ver las primeras filas de la categoria comestibles
vol = fin[fin.Categoría == "Comestibles"]
print(vol.head())

#Contar la cantidad de articulos de la categoria comestibles
print(vol.Artículo.value_counts())

#Grafico de barras, barras laterales, de torta, de puntos

vol.Artículo.value_counts().plot(kind = 'bar', color = "green", figsize = (10,5));

#vol.Artículo.value_counts().plot(kind = 'barh', color = "red");

#vol.Artículo.value_counts().plot(kind = 'pie');

#fin.plot(kind = "scatter", x = "Unidades", y = "Ganancia")

plt.show()





