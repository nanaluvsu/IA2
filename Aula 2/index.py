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

def fy(arr1,arr2):
    slope = w(arr1,arr2)
    intercept = b(arr1,arr2)
    y = []
    for i in range(len(arr1)):
        y.append(round((slope * arr1[i]) + intercept, 2))

    return y
       
def mse(arr1,arr2):
    predicts = fy(arr1,arr2)
    diffs = []
    
    for i in range(len(arr2)):
        diffs.append(round(arr2[i] - predicts[i],2))
    
    sqrdiffs = round(sum(i ** 2 for i in diffs),2)
    
    mse = round((1*sqrdiffs)/len(arr1),2)
    return mse
        
        

def q2():
    x = [1,1.5,2,2.5,3]
    y = [366,550,740,890,1090]    
    print(mse(x,y))
    time.sleep(2)
    print("Dados reais:")
    q2_dados()
    time.sleep(2)
    print("Comparativo - dados reais e modelo:")
    q2_comparativo()

def q2_dados():
    x = [1,1.5,2,2.5,3]
    y = [366,550,740,890,1090]

    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, color='blue', label='Dados reais')
    plt.title('Q2 - Dados reais')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.legend()
    plt.show()

def q2_comparativo():
    x = [1,1.5,2,2.5,3]
    y = [366,550,740,890,1090]
    y_est = fy(x, y)

    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, color='blue', label='Dados reais')
    plt.plot(x, y_est, color='red', linewidth=2, label='Modelo estimado')
    plt.title('Q2 - Comparativo - dados reais e modelo')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.legend()
    plt.show()

def q3():
    x_alt = np.linspace ( 0 , 1 , 50)
    y_true = 10.7 * x_alt + 5.8 + np.random.randn(50) * 8.6
    x_alt = x_alt.tolist()
    y_true = y_true.tolist()
    print("Dados reais:")
    q3_dados()
    time.sleep(2)
    print("Comparativo - dados reais e modelo:")
    q3_comparativo()

def q3_dados():
    np.random.seed(42)
    x_alt = np.linspace(0, 1, 50)
    y_true = 10.7 * x_alt + 5.8 + np.random.randn(50) * 8.6

    plt.figure(figsize=(8, 5))
    plt.scatter(x_alt, y_true, color='blue', label='Dados reais')
    plt.title('Questão 3 - Dados reais')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.legend()
    plt.show()

def q3_comparativo():
    np.random.seed(42)
    x_alt = np.linspace(0, 1, 50)
    y_true = 10.7 * x_alt + 5.8 + np.random.randn(50) * 8.6
    x_alt = x_alt.tolist()
    y_true = y_true.tolist()
    y_est = fy(x_alt, y_true)

    plt.figure(figsize=(8, 5))
    plt.scatter(x_alt, y_true, color='blue', label='Dados reais')
    plt.plot(x_alt, y_est, color='red', linewidth=2, label='Modelo estimado')
    plt.title('Questão 3 - Comparativo - dados reais e modelo')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.legend()
    plt.show()

    





if __name__ == "__main__":
    q2()
    time.sleep(3)
    q3()