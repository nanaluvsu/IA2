import math
import operator
import numpy as np
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
    y = []
    for i in range(len(arr1)):
        y.append(round((w(arr1,arr2) * arr1[i]),2) + 12)
    
    
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

def q3():
    x_alt = np.linspace ( 0 , 1 , 50)
    y_true = 10.7 * x_alt + 5.8 + np.random.randn(50) * 8.6
    x_alt = x_alt.tolist()
    y_true = y_true.tolist()
    print(mse(x_alt,y_true))

    





if __name__ == "__main__":
    q2()