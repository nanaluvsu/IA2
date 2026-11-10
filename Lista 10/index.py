import seaborn as sns
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import time
pd.options.display.float_format = '{:.2f}'.format

def regressao(x,y):
    reg_lin = LinearRegression().fit(x,y)
    w = reg_lin.coef_[0]
    b = reg_lin.intercept_
    print("w: " + str(w))
    print("b: " + str(b))
    print("\n")
    predict = reg_lin.predict(x)
    print(predict)
    
    plt.figure(figsize=(8, 6))
    
    return predict
    
def params():
    df = pd.read_csv('Real estate.csv')
    x = df[["X2 house age"]]
    y = df[["Y house price of unit area"]]
    
    return df,x,y

def compare():
    df = params()[0]
    y = params()[2]
    predictions = []
    for prediction in q1():
        predictions.append(prediction)
    for prediction in q2():
            predictions.append(prediction)
    for prediction in q3():
            predictions.append(prediction)
    
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data = predictions, x="y predito", y="y")
    plt.show()

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
    '''Responder depois'''
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
    return reg_q2
    
def q3():
    df = params()[0]
    x = df[["X1 transaction date","X2 house age","X3 distance to the nearest MRT station","X4 number of convenience stores","X5 latitude","X6 longitude"]]
    y = params()[2]
    reg_q3 = regressao(x,y)
    return reg_q3

q1()
q2()
q3()