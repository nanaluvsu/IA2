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
             print("vc e burro smt")
        
ex1()