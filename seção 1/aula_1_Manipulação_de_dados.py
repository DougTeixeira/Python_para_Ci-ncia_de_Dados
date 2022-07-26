import numpy as np
import pandas as pd
from pandas import Series, DataFrame

#criar dados

dados = np.arange(8) # cria um array de 0 ate 7
print(dados)

print(dados.reshape((4,2))) #re-organiza os dados, deixando ele com 4 linhas e 2 colunas

indice = ['linha 1', 'linha 2', 'linha 3', 'linha 4',
 'linha 5', 'linha 6', 'linha 7', 'linha 8']

series = Series(dados, index=indice) # organizar o array com indices
print(series)
print(series['linha 6'])
print(series['linha 3':'linha 7'])


np.random.seed(25)
indice = ['linha 1', 'linha 2', 'linha 3', 'linha 4', 'linha 5', 'linha 6']
colunas = ['coluna 1', 'coluna 2', 'coluna 3', 'coluna 4', 'coluna 5', 'coluna 6']

df = DataFrame(np.random.rand(36).reshape((6,6)), index=indice, columns=colunas)
print(df)

print(df.loc[['linha 2', 'linha 4'], ['coluna 3', 'coluna 5']])