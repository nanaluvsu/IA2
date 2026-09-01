import seaborn as sns
import pandas as pd
import scipy.stats as stats
import time
pd.options.display.float_format = '{:.2f}'.format
df = sns.load_dataset("planets")
print("Dataset carregado eba")

def normalizacao(df):
    df_normalized= df.select_dtypes(include=['float64']).copy()
    df_normalized = (df_normalized - df_normalized.min()) / (df_normalized.max() - df_normalized.min())

    return df_normalized

def eliminar_nulos(df, op):
    df_eliminado = df.copy()
    if op == 0:
        df = df_eliminado.dropna(axis=0) #linhas com valores nulos
    elif op == 1:
        df = df_eliminado.dropna(axis=1) #colunas com valores nulos
    else:
        print("Opção inválida")
    return df
    
def substituicao(op): #Obedecendo à solicitação "Considere utilizar a função fillna()".
    match op:
        case 1: #substituição por média
            return df.fillna(df.mean(numeric_only=True))
        case 2: #substituição por mediana
            return df.fillna(df.median(numeric_only=True))
        case 3: #substituição por moda
            return df.fillna(df.mode().iloc[0])
        case 4: #substituição por 0
            return df.fillna(0)
        case 5: #substituição por valor digitado pelo usuário
            valor = float(input("Digite o valor a substituir campos inválidos: "))
            return df.fillna(valor)
        case 6: #substituição pelo valor anterior
            return df.ffill() #parâmetro ffill foi alterado para o método ffill(). Mesmo se aplica para bfill
        case 7: #substituição pelo valor posterior
            return df.bfill()
        
def zscore(df):
    df_zscore = df.copy()
    cols = ['orbital_period', 'mass', 'distance'] # Obedecendo à solicitação "Utilize as colunas orbital_period, mass e distance para verificar se a função foi implementada corretamente."
    df_zscore[cols] = df_zscore[cols].apply(stats.zscore)
    return df_zscore

print(df.head())
print("\n\n\n" + "Informações do dataset: \n")
print(df.describe())
print("\n\n\n" + "Valores únicos: \n")
print(df.nunique())
print("\n\n\n" + "Tipos das tabelas: \n")
print(df.dtypes)
print("\n\n\n" + "Valores nulos: \n")
print(df.isnull().sum())
print("\n\n\n" + "Opções: ")
print("1 - Eliminar linhas/colunas com valores nulos")
print("2 - Substituir valores nulos")
opcao = int(input("Digite a opção desejada: "))
if opcao == 1:
    print("0 - Eliminar linhas com valores nulos")
    print("1 - Eliminar colunas com valores nulos")
    op = int(input("Digite a opção desejada: "))
    df_elim = eliminar_nulos(df, op)
    print("\n\n\n" + "Dataframe: (Cópia)\n")
    print(df_elim)
elif opcao == 2:
    print("1 - Substituição por média")
    print("2 - Substituição por mediana")
    print("3 - Substituição por moda")
    print("4 - Substituição por 0")
    print("5 - Substituição por valor digitado pelo usuário")
    print("6 - Substituição pelo valor anterior")
    print("7 - Substituição pelo valor posterior")
    op = int(input("Digite a opção desejada: "))
    df = substituicao(op)
    print("\n\n\n" + "Valores nulos após a substituição: \n")
    print(df.isnull().sum())
    print("\n\n\n" + "Dataframe: \n")
    print(df)
else: 
    print("Opção inválida")
time.sleep(2)
print("\n\n\n" + "Normalização: \n")
print(normalizacao(df))
time.sleep(2)
print("\n\n\n" + "Z-Score: \n")
print(zscore(df).to_string(float_format='{:,.6f}'.format))