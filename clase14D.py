# Selección

import pandas as pd
import os

ruta = os.path.abspath(os.path.dirname(__file__))

df = pd.read_csv(ruta+"/conMarcas.csv", encoding="utf-8")

dfPivoteado4 = pd.pivot_table(df, values=["Producto"], columns=[ "SumaPuntos", "Segmento"], index=["HayStock","Categoria"], aggfunc="count",   fill_value=0 )

# print(dfPivoteado4)

print(dfPivoteado4.loc[:,("Producto", "SI", "BARATO")])