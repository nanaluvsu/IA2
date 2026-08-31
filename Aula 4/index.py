import seaborn as sns
import pandas as pd
import scipy.stats as stats
df = sns.load_dataset("planets")
print("Dataset carregado eba")

'''def normalizacao(df):
    df_normalized= (df - df.min())/(df.max()-df.min())

    return df_normalized'''


def zscore(df):
    cols = df.select_dtypes(include=['float64']).columns
    df[cols] = df[cols].apply(stats.zscore)
    return df
    
def substituicao(op):
    match op:
        case 1: #substituição por média
            df.fillna(df.mean(numeric_only=True))
            return df
        case 2: #substituição por mediana
            return df.fillna(df.median())
        case 3: #substituição por moda
            return df.fillna(df.mode())
        case 4: #substituição por 0
            return df.fillna(0)
        case 5: #substituição por valor digitado pelo usuário
            valor = float(input("Digite o valor a substituir campos inválidos: "))
            return df.fillna(valor)
        case 6: #substituição pelo valor anterior
            return df.fillna(method='ffill')
        case 7: #substituição pelo valor posterior
            return df.fillna(method='bfill')

print(df.head())
print("\n\n\n" + "Informações do dataset: \n")
print(df.describe())
print("\n\n\n" + "Valores únicos: \n")
print(df.nunique())
print("\n\n\n" + "Valores nulos: \n")
print(df.isnull().sum())
print("\n\n\n" + "Tipos das tabelas: \n")
print(df.dtypes)

print("\n\n\n" + "Z-Score: \n")
print(zscore(df))
#print("\n\n\n" + "Normalização: \n")
#print(normalizacao(df))
print("\n\n\n" + "Substituição de valores nulos: \n")
print("Opções: ")
print("1 - Substituição por média")
print("2 - Substituição por mediana")
print("3 - Substituição por moda")
print("4 - Substituição por 0")
print("5 - Substituição por valor digitado pelo usuário")
print("6 - Substituição pelo valor anterior")
print("7 - Substituição pelo valor posterior")
ans = int(input("Digite a opção desejada: "))
print(substituicao(ans))