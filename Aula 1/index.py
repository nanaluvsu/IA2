def ex1():
    '''
    Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles
    estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for
    lido um número negativo.
    '''
    b1 = []
    b2 = []
    b3 = []
    b4 = []
    ans = 0
    while ans >=0:
        ans = int(input('oi q numero:\n'))
        if (ans >= 0 and ans <= 25):
             b1.append(ans)
        elif (ans >= 26 and ans <= 50):
             b2.append(ans)
        elif (ans >= 51 and ans <= 75):
             b3.append(ans)
        elif (ans >= 76 and ans <= 100):
             b4.append(ans)
        elif (ans <= 0):
            print("Bloco 1 - [0-25]\n")
            for item in b1:
                print(item)
            print("Bloco 2 - [26-50]\n")
            for item in b2:
                print(item)
            print("Bloco 3 - [51-75]\n")
            for item in b3:
                print(item)
            print("Bloco 4 - [76-100]\n")
            for item in b4:
                print(item) 
            break #ae break pode fazer 50000 video sobre o oliver tree
        
        else:
             print("vc e burra (ou burro sem preconceito)")

def ex2():
    '''
    Escreva uma função que receba uma lista de números e retorne um dicionário contendo a contagem
    de ocorrências de cada número na lista.
    '''
    def dict_qtd(lista):
        dict_qtds = {}
        lista = list(lista)
        for item in lista:
            if item not in dict_qtds:
                dict_qtds[item] = lista.count(item)
        return dict_qtds


    lista_ex2 = [5,5,5,5,4,4,3,3,3,3,3,2,1,67]
    print(dict_qtd(lista_ex2))

def ex3():
    '''
    Considere o seguinte conjunto:
    Z = {5, 2, 11, 8, 3, 8, 7, 4}
    a) Crie um código em Python para realizar o cálculo do desvio padrão de Z sem utilizar bibliotecas e funções
    matemáticas prontas para resolver o problema.
    b) Utilize as funções disponíveis nas bibliotecas numpy e statistics e faça a conferência dos resultados
    '''           

    Z = [5,2,11,8,3,8,7,4]

    
        
print("oi qual exercicio vc quer")
ex = int(input())

match(ex):
    case 1:
        ex1()
    case 2: 
        ex2()
    case 3: 
        ex3()
    case 4:
        ex4()
    case 5:
        ex5()
    case 6:
        ex6()
    case 7:
        ex7()
    case 8:
        ex8()
    case 9: 
        ex9()
    case 10:
        ex10()
    case _:
        print("vc e burra (ou burro sem preconceito) smt")