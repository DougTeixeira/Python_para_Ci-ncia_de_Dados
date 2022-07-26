import numpy as np
import pandas as pd
from pandas import Series, DataFrame

dados = {
    'coluna 1': [1, 1, 2, 2, 3, 3],
    'coluna 2': ['a', 'a', 'b', 'b', 'c', 'c'],
    'coluna 3': ['A', 'A', 'B', 'B', 'C', 'C'],
}

df = DataFrame(dados)
print(df)

print(df.duplicated()) # verifica de linha com linha para saber se alguma é repetida

print(df.drop_duplicates()) # traz um novo df sem as duplicatas

df.drop_duplicates(inplace=True) # substitui o df com repetições por um df sem
print(df)


dados = {
    'coluna 1': [1, 1, 2, 2, 3, 3, 3],
    'coluna 2': ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
    'coluna 3': ['D', 'A', 'B', 'B', 'C', 'C', 'C'],
}

df = DataFrame(dados)
print(df)
print(df.drop_duplicates(['coluna 3'])) # leva em consideração apenas a coluna 3