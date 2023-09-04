import numpy as np
import random

def sigmoid(x):
    return 1 / (1+ np.exp(-x))

def derivada_sigmoid(x):
    return x * (1 - x)

passo = 0.5

while True:
    porta = input("Inisra o tipo de porta (AND/OR/XOR): ")

    if(porta == "AND" or porta == "and"):
        porta = "AND"
        X = np.array([[0,0],
                      [0,1],
                      [1,0],
                      [1,1]])

        Y = np.array([[0],
                      [0],
                      [0],
                      [1]])
        break
        
    elif(porta == "OR" or porta == "or"):
        porta = "OR"
        X = np.array([[0,0],
                      [0,1],
                      [1,0],
                      [1,1]])

        Y = np.array([[0],
                      [1],
                      [1],
                      [1]])
        break
        
    elif(porta == "XOR" or porta == "xor"):
        porta = "XOR"
        X = np.array([[0,0],
                      [0,1],
                      [1,0],
                      [1,1]])

        Y = np.array([[0],
                      [1],
                      [1],
                      [0]])
        break

    else:
        print("Insira uma porta válida!")

camada_entrada = 2
camada_oculta = 4
camada_saida = 1

w1 = 2 * np.random.random((camada_entrada, camada_oculta)) - 1
w2 = 2 * np.random.random((camada_oculta, camada_saida)) - 1

epoca = 0
epocas = 10000
acuracia = 0

while acuracia < 100 and epoca < epocas:
    entrada_oculta = np.dot(X, w1)
    saida_oculta = sigmoid(entrada_oculta)

    entrada_saida = np.dot(saida_oculta, w2)
    saida_saida = sigmoid(entrada_saida)

    erro = Y - saida_saida

    delta_saida = erro * derivada_sigmoid(saida_saida)

    erro_oculta = delta_saida.dot(w2.T)

    delta_oculta = erro_oculta * derivada_sigmoid(saida_oculta)

    w2 += saida_oculta.T.dot(delta_saida) * passo 
    w1 += X.T.dot(delta_oculta) * passo

    saida_esperada = (saida_saida > 0.5).astype(int)
    acuracia = 100 * np.sum(saida_esperada == Y) / len(Y)

    epoca += 1

    print(f"Época {epoca + 1}/{epocas} - Acurácia atual: {acuracia:.2f}%")

print("\nPesos e bias final:")
print("Pesos da camada de entrada para a camada oculta:")
print(w1)
print("\nPesos da camada oculta para a camada de saida:")
print(w2)

print("\nTestando com acurácia de 100%")

while True:
    x1 = int(input("X1: "))
    x2 = int(input("X2: "))

    if x1 > 0:
        x1 = 1
    else:
        x1 = 0

    if x2 > 0:
        x2 = 1
    else:
        x2 = 0

    entrada_oculta = np.dot(np.array([[x1, x2]]), w1)
    saida_oculta = sigmoid(entrada_oculta)
    entrada_saida = np.dot(saida_oculta, w2)
    saida_saida = sigmoid(entrada_saida)

    saida_esperada = (saida_saida > 0.5).astype(int)

    print(f"\n{x1} {porta} {x2} -> {saida_esperada[0][0]}\n")

    if input("E-(Exit) T-(Try Again): ").lower() == 'e':
        break

print("\nTeste concluído.")

