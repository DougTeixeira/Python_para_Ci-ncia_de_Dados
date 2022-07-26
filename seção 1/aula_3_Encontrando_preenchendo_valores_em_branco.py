import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# encontrando valores em branco
em_branco = np.nan
serie = Series(['linha 1', 'linha 2', em_branco, 'linha 4', 'linha 5', 'linha 6', em_branco, 'linha 8'])
print(serie)

print(serie.isnull()) # retorna true para quando achar valores NaN

#preenchendo valores em branco
np.random.seed(25)
df = DataFrame(np.random.rand(36).reshape((6,6)))
print(df)
df.loc[3:5, 0] = em_branco
df.loc[1:4, 5] = em_branco
print(df)

df_preenchido = df.fillna(0) # preenchendo com zeros
print(df_preenchido)

dicio = {0: 0.1, 5: 1.25} # quem for NaN na linha 0 e 5 será substituido pelos valores escolhidos
df_preenchido = df.fillna(dicio) # preenchendo com valores do dicionario criado
print(df_preenchido)

