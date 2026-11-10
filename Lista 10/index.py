import seaborn as sns
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import time
pd.options.display.float_format = '{:.2f}'.format

def regressao(x,y):
    X_treino, X_teste, Y_treino, Y_teste = train_test_split(x, y, test_size=0.2, random_state=42)

    reg_lin = LinearRegression().fit(X_treino, Y_treino)

    w = reg_lin.coef_[0]
    b = reg_lin.intercept_

    for i, coef in enumerate(w):
        print(f"w{i+1}: {coef}")

    print("b:", b)
    
    predict = reg_lin.predict(X_teste)

    print("\nPrevisões:")
    print(predict)

    mse = mean_squared_error(Y_teste, predict)
    mae = mean_absolute_error(Y_teste, predict)
    r2 = r2_score(Y_teste, predict)

    print("MSE:", mse)
    print("MAE:", mae)
    print("R²:", r2)

    return predict
    
def params():
    df = pd.read_csv('Real estate.csv')
    x = df[["X2 house age"]]
    y = df[["Y house price of unit area"]]
    
    return df,x,y



def q1():
    df = params()[0]
    print("Q1")
    print("\n")

    print("===========")
    print("a)")
    
    print("csv carregado.")
    print("\n")

    print("===========")
    print("b)")
    df.info()
    print("\n")


    print("Shape:")
    print(df.shape)
    print("\n")

    print("===========")
    print("c)")
    x = params()[1]
    y = params()[2]

    print("\n")
    print("===========")
    print("d)")
    X_treino, X_teste, Y_treino, Y_teste = train_test_split(x, y, test_size=0.2, random_state=42)
    print("X - treino")
    print(X_treino)
    print("\n")

    print("X - teste")
    print(X_teste)
    print("\n")

    print("Y - treino")
    print(Y_treino)
    print("\n")

    print("Y - teste")
    print(Y_teste)
    print("\n")

    print("===========")
    print("e)")
    print("Resposta comentada")
    '''A função train_test_split recebe dados de 2 vetores e os embaralha aleatoriamente, baseando-se no "random_state"
depois, ela separa os registros com base num indice indicado, "test_size"

por fim, os resultados gerados sao 2 conjuntos de x e y, sendo um conjunto de treino e outro de teste.'''
    print("\n")

    print("===========")
    print("f)")
    reg_q1 = regressao(x,y)
    return reg_q1

def q2():
    df = params()[0]
    y = params()[2]
    x = df[["X3 distance to the nearest MRT station"]] 
    
    reg_q2 = regressao(x,y)

    print("Explicação comentada")
    '''Em q1, o modelo utiliza a idade dos imóveis como variável independente (X2), enquanto em q2 utiliza a distância até a estação MRT mais próxima(X3).
       Ao comparar os resultados, é possível observar qual variável apresenta melhor relação linear com o preço dos imóveis. O modelo que apresentar menores valores de MSE e MAE e maior valor de R² terá melhor desempenho nos dados avaliados.
       As diferenças entre os coef. angulares também demonstram como cada variável influencia o preço previsto.'''
    return reg_q2
    
def q3():
    df = params()[0]
    x = df[["X1 transaction date","X2 house age","X3 distance to the nearest MRT station","X4 number of convenience stores","X5 latitude","X6 longitude"]]
    y = params()[2]
    reg_q3 = regressao(x,y)
    print("Explicação comentada")
    '''A Regressão Linear Multivariável é um método estatístico que utiliza várias variáveis de entrada para estimar um único resultado. Neste exercício, o modelo utiliza as seis características dos imóveis (data da transação, idade, distância até a estação MRT, número de lojas de conveniência, latitude e longitude) para prever o preço por unidade de área.

       Diferentemente da regressão linear simples, que considera apenas uma variável de entrada, a multivariável analisa todas essas características simultaneamente, permitindo considerar a influência de cada uma na previsão.

       O modelo apresentou um desempenho superior aos modelos anteriores, pois conseguiu utilizar mais informações sobre os imóveis para realizar as previsões.'''
    return reg_q3

q1()
q2()
q3()
