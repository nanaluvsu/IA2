import math
import operator
import numpy as np
import time
import subprocess
import matplotlib.pyplot as plt
import mq


def dw(arr1,arr2,w,b):
    predicts = predicoes(arr1,w,b)
    diffs = []
    for i in range(len(predicts)):
        diffs.append((arr1[i]) * (predicts[i] - arr2[i]))

    dw = (2/len(arr2)) * sum(diffs)
    return dw    

def db(arr1,arr2,w,b):
    predicts = predicoes(arr1,w,b)
    diffs = []
    for i in range(len(predicts)):
        diffs.append(predicts[i] - arr2[i])

    db = (2/len(arr2)) * sum(diffs)
    return db    
    
def mse(arr1,arr2,w,b):
    predicts = predicoes(arr1,w,b)
    diffs = []
    for i in range(len(arr2)):
        diffs.append(arr2[i] - predicts[i])
    
    sqrdiffs = sum(i ** 2 for i in diffs)
    mse = (1*sqrdiffs)/len(arr1)
    return mse

def slope(arr1,arr2,w,b,taxa):
    w1 = round(w - taxa * dw(arr1,arr2,w,b), 2)
    #w1 = w - taxa * dw(arr1,arr2,w,b)
    return w1
    
def intercept(arr1,arr2,w,b,taxa):
    b1 = round(b - taxa * db(arr1, arr2, w, b), 2)
    #b1 = b - taxa * db(arr1, arr2, w, b)
    return b1

def gradiente(arr1, arr2, w, b, taxa, count):
    while count <= 5000:
        print("Iteração " + str(count) + " começando.")
        print("MSE para a iteração: " + str(round(mse(arr1, arr2, w, b), 2)))
        new_w = slope(arr1, arr2, w, b, taxa)
        new_b = intercept(arr1, arr2, w, b, taxa)
        w = new_w
        b = new_b
        count += 1

    return w, b

def graph_dados(questao, x, y):
    import matplotlib.pyplot as plt
    plt.scatter(x, y, color='blue', label='Dados reais')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Questão " + str(questao) + " - Dados reais")
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.show()

def graph_comparativo(questao, x, y, w, b):

    y_est = predicoes(x, w,b)

    plt.scatter(x, y, color='blue', label='Dados reais')
    plt.plot(x, y_est, color='red', linewidth=2, label='Modelo estimado')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.title("Questão " + str(questao) + " - Comparativo - dados reais e modelo")
    plt.legend()
    plt.show()

def predicoes(arr1,w,b):
    y_arr = []
    
    for i in range(len(arr1)):
        y = float((w*arr1[i])+b)
        y_arr.append(y)
    return y_arr

def q2():
    print("\n===============\n\nQuestão 2\n\n===============\n")
    x = [1, 1.5, 2, 2.5,3]
    y = [366, 550, 740, 890, 1090]
    w0 = float(input("Insira o valor inicial de w: "))
    b0 = float(input("Insira o valor inicial de b: "))
    taxa = float(input("Insira a taxa de aprendizado: "))
    w, b = gradiente(x,y,w0,b0,taxa,0)
    graph_dados(2,x,y)
    graph_comparativo(2,x,y,w,b)

q3_q4x = np.linspace(0,1,50)
q3_q4y = 7.52 * q3_q4x + 3.36 + np.random.randn(50) * 12.5
def q3():
    print("\n=============================================\n")
    
    x = q3_q4x.tolist()
    y = q3_q4y.tolist()
    
   
    w0 = float(input("Insira o valor inicial de w: "))
    b0 = float(input("Insira o valor inicial de b: "))
    taxa = float(input("Insira a taxa de aprendizado: "))
    w, b = gradiente(x,y,w0,b0,taxa,0)
    print("w =", round(w, 2))
    print("b =", round(b, 2))
    graph_dados(3,x,y)
    graph_comparativo(3,x,y,w,b)


def q4():
    print("\n=============================================\n")
    x = q3_q4x.tolist()
    y = q3_q4y.tolist()
    w_mq = mq.w(x, y)
    b_mq = mq.b(x, y) 
    '''
    w = 4.7
    b = 5.18
    '''
    

    print("w =", round(w_mq, 2))
    print("b =", round(b_mq, 2))
    
    print("Predições: " + str(mq.predicoes(x,y)))
    print("MSE: " + str(mq.mse(x,y)))
    mq.graph_dados(4,x,y)
    mq.graph_comparativo(4,x,y)

def q5():
    print("\n===============\n\nQuestão 5\n\n===============\n")
    print("Resposta: ")
    print("Os métodos de Mínimos Quadrados (Least Squares) e Gradiente Descendente (Gradient Descent) utilizam os mesmos dados de entrada nas questões 3 e 4,")
    print("porém chegaram a valores diferentes para w e b. Isso ocorre porque, apesar de utilizarem os mesmos dados, os métodos calculam os parâmetros de slope e intercept(w e b) de formas diferentes.")
    print("No Gradiente Descendente, w e b são atualizados iterativamente e arredondados para duas casas decimais a cada iteração, enquanto nos Mínimos Quadrados")
    print("os parâmetros são calculados diretamente por meio das fórmulas do método.")
    print("Isso pode ser observado nos resultados obtidos e também nos gráficos, pois as retas estimadas apresentam claras inclinações distintas.")
q2()
q3()
q4()
q5()