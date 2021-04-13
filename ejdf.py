import pandas as pd

df = pd.read_csv(r"C:\Users\LENOVO\PycharmProjects\Practica Pandas - Matplotlib\dataframe.csv")
print(df)

#Nombres de columnas
columns_names = df.columns.values
print(columns_names)

#Columna determinada y el tipo
print(df.Nombre)
print(type(df.Nombre))

#Cantidad de filas y columnas, primeras 3 filas, últimas 3 filas, información del DataFrame
print(df.shape)
print(df.head(3))
print(df.tail(3))
df.info()

#Cantidad de veces que se repite el valor de una columna
print(df.Automovil.value_counts())

#Ordenar la columna de manera descendente y sin valores nulos
print(df.Automovil.value_counts(ascending=False, dropna=False))

#Ordenar alfabéticamente una columna
print(df.Pais.sort_values())

#Ordenar alfabéticamente dos columnas, primero lo ordena por la primer columna y si el dato se repite lo ordena por la segunda columna
print(df.sort_values(by=["Nombre", "Pais"]))

#Filtrar información
print(df[df.Pais == "Argentina"])
print(df[(df.Pais == "Colombia") & (df.Automovil == "No")])
print(df[df.Pais.str.contains("Peru")]) #Palabra dentro de columna
print(df[df.Pais.str.contains("H")])    #Letra dentro de columna

#Cambiar el indice (ordenamiento de datos), y que quede fijado por la columna que indico
df.set_index("Pais", inplace=True)
print(df)
df.reset_index(inplace=True)  #Para volver al indice anterior
print(df)

#Creo DataFrame con nuevo indice
Pais = df.set_index("Pais")
print(Pais)

#Localizar por etiqueta
print(df.loc[df.Pais == "Peru"])
print(Pais.loc["Argentina"])

#Agrupar por indices numericos
print(df.iloc[[0, 5, 8]])
print(df.iloc[1:7])

#Agrupar por datos dependiendo de la columna
print(list(df.groupby("Automovil")))

#Agrupar por medio de la llave (En Automovil es si/no) y el valor (indice)
for group_key, group_value in df.groupby("Automovil"):
    print(group_key)
    print(group_value)

#Diferentes agrupaciones con groupby
print(df.groupby(["Edad", "Pais"]).agg({"Edad": ["min", "max", "count"]}))

#Filtrar
filtrar = df[((df.Pais == "Colombia") | (df.Pais == "Argentina")) & (df.Automovil == "Si")]
print(filtrar)

#Agrupar
agrupar = filtrar.groupby(["Pais", "Automovil"]).size()
print(agrupar)

#Unstack
unstack = agrupar.unstack("Automovil")
print(unstack)



