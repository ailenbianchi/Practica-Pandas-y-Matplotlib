import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patheffects as pa

#Uso el sep debido a que el archivo esta en formato excel y quiero separarlo por ;
fin2 = pd.read_csv(r"C:\Users\LENOVO\PycharmProjects\Practica Pandas - Matplotlib\finanzas2.csv", sep = ";")

fin2.info()

#Debido a que el formato de la fecha no es el que requiero, lo cambio
fin2["Fecha"] = pd.to_datetime(fin2["Fecha"], format= "%d/%m/%Y")
fin2.info()

#Pongo como indice la fecha
fin2.set_index("Fecha", inplace=True)
print(fin2.head(10))

#Usando ggplot, otro estilo de matplotlib
plt.style.use("ggplot")

fig, ax = plt.subplots(figsize = (12,10))

ax.plot(fin2["Elon Mosk"], label = "Elon Mosk", lw = 2, color = "orange", path_effects = [pa.SimplePatchShadow(), pa.Normal()])
ax.plot(fin2["Bill Gate"], label = "Bill Gate", lw = 2, color = "brown", linestyle = "-.", path_effects = [pa.SimplePatchShadow(), pa.Normal()])

ax.legend(shadow = True, prop = {"family": "Serif", "size": "15"})

ax.set_ylabel("USD", fontname = "Serif", fontsize = "20")
ax.set_xlabel("Time", fontname = "Serif", fontsize = "20")
ax.set_title("Elon Mosk vs Bill Gate", fontname = "Serif", fontsize = "25")

plt.show()



