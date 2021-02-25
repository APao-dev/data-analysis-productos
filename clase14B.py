import pandas as pd
import os

ruta = os.path.abspath(os.path.dirname(__file__))

df = pd.read_csv(ruta+"/conMarcas.csv", encoding="utf-8")

print(df[["Producto", "Marca"]].head(50))

print(df[df["Precio"]>200])

print(df[df["Precio"]>200][["Producto", "Precio"]])


print(df[df["Precio"]>200][["Producto", "Precio"]].count())

df["PrecioNuevo"] = 100
print(df[["Producto", "PrecioNuevo"]])

# Aumentar en 500% el precio de los productos
df["PrecioInflacion"]=False
df[df["Marca"]=="Watson"]["PrecioInflacion"] = df["Precio"]*5
print("Hola fin")

print(df[df["Marca"]=="Watson"][["Precio", "PrecioInflacion]"]])

# Soluciones
df["PrecioInflacion"] = df.apply(..........)

# Selección por .LOC (es la más profesional)

