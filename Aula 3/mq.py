import math
import operator
import numpy as np
import matplotlib.pyplot as plt
import time
def w(arr1,arr2):
    xi = sum(arr1) # no caso de x, 10
    yi = sum(arr2) # no caso de y, 3636
    sqrxi = sum(i ** 2 for i in arr1)
    xiyi = sum(list(map(operator.mul,arr1,arr2)))
    
    w = ((len(arr1)*xiyi) - xi*(yi))/((len(arr1)*sqrxi) - xi ** 2)
    
    return w

def b(arr1,arr2):
    b = (sum(arr2) - w(arr1,arr2)*sum(arr1))/len(arr1)
    return b

def predicoes(arr1,arr2):
    slope = w(arr1,arr2)
    intercept = b(arr1,arr2)
    y = []
    for i in range(len(arr1)):
        y.append(round((slope * arr1[i]) + intercept, 2))

    return y
       
def mse(arr1,arr2):
    predicts = predicoes(arr1,arr2)
    diffs = []
    
    for i in range(len(arr2)):
        diffs.append(round(arr2[i] - predicts[i],2))
    
    sqrdiffs = round(sum(i ** 2 for i in diffs),2)
    
    mse = round((1*sqrdiffs)/len(arr1),2)
    return mse




def graph_dados(questao, x,y):
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, color='blue', label='Dados reais')
    plt.title("Questão " + str(questao) + " - Dados reais")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.legend()
    plt.show()

def graph_comparativo(questao, 
                      x,y):
    y_est = predicoes(x, y)

    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, color='blue', label='Dados reais')
    plt.plot(x, y_est, color='red', linewidth=2, label='Modelo estimado')
    plt.title("Questão " + str(questao) + " - Comparativo - dados reais e modelo")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.legend()
    plt.show()