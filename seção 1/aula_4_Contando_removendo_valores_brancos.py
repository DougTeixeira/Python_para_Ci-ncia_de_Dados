import numpy as np
import pandas as pd
from pandas import Series, DataFrame

em_branco = np.nan
np.random.seed(25)
df = DataFrame(np.random.rand(36).reshape(6,6))
print(df)
df.loc[3:5, 0] = em_branco
df.loc[1:4, 5] = em_branco
print(df)

# contando os valores em branco
print(df.isnull().sum()) # mostra o indice da coluna a esquerda e a quantidade de NaN na direita

print(df.dropna()) # retorna as unicas linhas q n possuem nenhuma coluna com NaN

print(df.dropna(axis=1)) # retorna as colunas q n tem nenhum NaN