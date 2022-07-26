import numpy as np
import pandas as pd
from pandas import Series, DataFrame

np.random.seed(25)

indice = ['linha 1', 'linha 2', 'linha 3', 'linha 4', 'linha 5', 'linha 6']
colunas = ['coluna 1', 'coluna 2', 'coluna 3', 'coluna 4', 'coluna 5', 'coluna 6']

df = DataFrame(np.random.rand(36).reshape((6,6)), index=indice, columns=colunas)
print(df)

# comparando um valor
print(df < 0.2) # comparando valores para o recebindo de um dt com boleano


# valor escalar para filtrar
indice = ['linha 1', 'linha 2', 'linha 3', 'linha 4', 'linha 5', 'linha 6', 'linha 7', 'linha 8']
series_obj = Series(np.arange(8), index=indice)

filtro = series_obj > 5 # salvando os valores maiores q 5 com boleano
print(filtro)
print(series_obj[filtro]) # mostrando os valores q foram True

#atualizando valores
series_obj['linha 1', 'linha 5', 'linha 8'] = 8
print(series_obj)