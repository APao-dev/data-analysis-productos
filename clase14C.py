import pandas as pd
import os

ruta = os.path.abspath(os.path.dirname(__file__))

df = pd.read_csv(ruta+"/conMarcas.csv", encoding="utf-8")

dfPivoteado4 = pd.pivot_table(df, values=["Producto"], columns=[ "SumaPuntos", "Segmento"], index=["HayStock","Categoria"], aggfunc="count",   fill_value=0 )
# print(dfPivoteado4)

# Seleccion simple con .LOC

# [filaDesde:filaHasta,[lista de columnas]]
# print(df.loc[203:250])
#  Seleccionar un producto
# print(df.loc[301])

# Seleccionar algunas columnas de un producto
# print(df.loc[301,["Marca", "Precio"]])

# Seleccionar los productos a partir del 280
# print(df.loc[280:,["Producto"]])


# Seleccionar COLUMNAScon .loc[] sin importar FILAS

# print(df.loc[:,["Producto", "Precio"]]) #es lo que más se hace :,


# Selección por .loc con filtro

# print(df.loc[df["Marca"]=="Watson"][["Producto", "Precio"]])

df.loc[df["Marca"] == "Watson", ["PrecioInflacion"]]= df["Precio"]*5

print()