import pandas as pd
import os

ruta = os.path.abspath(os.path.dirname(__file__))

df = pd.read_csv(ruta+"/conMarcas.csv", encoding="utf-8")

# print(df)

# dfPivoteado = pd.pivot_table(df, values=["Producto"], columns=["Segmento"], index=["Categoria"], aggfunc="count", fill_value=0  margins=True, margins=)

# print(dfPivoteado)

dfPivoteado2 = pd.pivot_table(df, values=["Producto"], columns=["Segmento"], index=["Categoria", "HayStock"], aggfunc="count",   fill_value=0 )

# print(dfPivoteado2)


dfPivoteado3 = pd.pivot_table(df, values=["Producto"], columns=["Segmento"], index=["HayStock","Categoria"], aggfunc="count",   fill_value=0 )
# print(dfPivoteado3)

dfPivoteado4 = pd.pivot_table(df, values=["Producto"], columns=[ "SumaPuntos", "Segmento"], index=["HayStock","Categoria"], aggfunc="count",   fill_value=0 )
# print(dfPivoteado4)

dfPivoteado5 = pd.pivot_table(df, values=["Producto"], columns=[ "Segmento","SumaPuntos"], index=["HayStock","Categoria"], aggfunc="count",   fill_value=0 )
# print(dfPivoteado5)

dfPivoteado6 = pd.pivot_table(df, values=["Producto", "Precio"], columns=[ "SumaPuntos"], index=["HayStock","Categoria"], aggfunc={"Producto": "count", "Precio": "mean"},   fill_value=0 )
# print(dfPivoteado6)

# Subtotal

# Convertir a tabla simple "achatado"


# STACKING Y UNSTACKING

print(dfPivoteado4)
dfPivoteado4Stackeado = dfPivoteado4.stack()
# print(dfPivoteado4Stackeado.head(50))

dfPivoteado4Stackeado2 = dfPivoteado4.stack().stack()
# print(dfPivoteado4Stackeado2.head(50))


dfPivoteado4Unstackeado = dfPivoteado4.unstack()
# print(dfPivoteado4Unstackeado)

dfPivoteado4Stackeado2["Porcentaje"] = dfPivoteado4Stackeado2["Producto"]/dfPivoteado4Stackeado2["Producto"].sum()

# print(dfPivoteado4Stackeado2.head(50))



# Selección por CROSS SECTION

seleccionXs = dfPivoteado4.xs("BARATO", level="Segmento", axis=1)

print(seleccionXs)