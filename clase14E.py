

import pandas as pd
import os

ruta = os.path.abspath(os.path.dirname(__file__))

dfProductos = pd.read_csv(ruta+"/conMarcas.csv", encoding="utf-8")
dfMarcas = pd.read_csv(ruta+"/listaMarcas.csv", encoding="utf-8")

print(dfMarcas)

dfFusionado = pd.merge(dfProductos, dfMarcas, on="Marca")

# print(dfFusionado)

dfProductosPorDistribuidor = df