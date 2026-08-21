import math
import operator
import numpy as np
import time

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
    new = dw(arr1,arr2,w,b)
    w1 = round(w - taxa * new, 2)
    return w1
    
def intercept(arr1,arr2,w,b,taxa):
    b1 = round(b - taxa * db(arr1, arr2, w, b), 2)
    return b1

def gradiente(arr1,arr2,w,b,taxa, count):
    time.sleep(5)
    print("Iteração " + str(count) + " começando.")
    print(round(mse(arr1,arr2,w,b),2))
    new_w = slope(arr1,arr2,w,b,taxa)
    new_b = intercept(arr1,arr2,w,b,taxa)
    count+= 1
    gradiente(arr1,arr2,new_w,new_b,taxa,count)

def predicoes(arr1,w,b):
    y_arr = []
    
    for i in range(len(arr1)):
        y = float((w*arr1[i])+b)
        y_arr.append(y)
    return y_arr

x = [0,1,2]
y = [1,3,5]

w0 = float(input("Insira o valor inicial de w: "))
b0 = float(input("Insira o valor inicial de b: "))
taxa = float(input("Insira a taxa de aprendizado: "))
gradiente(x,y,w0,b0,taxa,0)