import numpy as np

def indentidade(n):
    m = []
    for i in range(0, n):
        linha = [0] * n
        linha[i] = 1
        m.append(linha)

    return m


def mostrarMatriz(linha, coluna, matriz, indentidade):
    for l in range(linha):
        for c in range(coluna):
            print(f'[{matriz[l][c]:^5}]', end='')
        for i in range(coluna):
            print(f'[{indentidade[l][i]:^5}]', end='')
        print()
        

def mostrarMatrizEscalonada(linha, coluna, matriz):
    for l in range(linha):
        for c in range(coluna):
            print(f'[{matriz[l][c]:^5}]', end='')
        print()


def matrizNula(linha, coluna):
    matriz = []
    for i in range(linha):
        matriz.append(list())
        for j in range(coluna):
            matriz[i].append(0)

    return matriz

def conferirMatrizNula(linha, coluna, matriz):
    cont = 0
    for i in range(linha):
        for j in range(coluna):
           if matriz[i][j] == 0:
               cont += 1 
    if cont == (linha * coluna):
        return True
    else:
        return False
    
def permutar(primeira_linha, segunda_linha, a):
    for j in range(len(a[0])):
        aux = a[primeira_linha][j]
        a[primeira_linha][j] = a[segunda_linha][j]
        a[segunda_linha][j] = aux

def linhaDivididoMultiplo(linha, multiplo, a):
    for j in range(len(a[linha])):
        a[linha][j] = a[linha][j] / multiplo
        
def linhaMaisOutraLinhaVezezMultiplo(primeira_linha, segunda_linha, multiplo, a):
    for j in range(len(a[0])): 
        operando1 = a[primeira_linha][j]
        operando2 = multiplo * a[segunda_linha][j]
        a[primeira_linha][j] = operando1 + operando2

def validarOperacaoPermuta(linha, coluna, a): 
        for i in range(linha + 1, len(a)):
            if a[i][coluna] != 0:
                return i
        
        return -1
    

def escalonarMatriz(matriz):
    colunaPivoAnterior = 0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if matriz[linha][coluna] == 0 and validarOperacaoPermuta(linha, coluna, matriz) != -1:
                permutar(linha, validarOperacaoPermuta(
                    linha, coluna, matriz), matriz)
                colunaPivoAnterior = coluna + 1

                print(mostrarMatrizEscalonada(
                    linhaMatriz, colunaMatriz, matriz))

                if matriz[linha][coluna] != 1:
                    multiplo = matriz[linha][coluna]
                    linhaDivididoMultiplo(linha, multiplo, matriz)

                print(mostrarMatrizEscalonada(
                    linhaMatriz, colunaMatriz, matriz))

                for j in range(linha + 1, len(matriz)):
                    if matriz[j][coluna] != 0:
                        multiplo = -1.0 * matriz[j][coluna]
                        linhaMaisOutraLinhaVezezMultiplo(
                            j, linha, multiplo, matriz)

                print(mostrarMatrizEscalonada(
                    linhaMatriz, colunaMatriz, matriz))

                if linha > 0:
                    for i in range(linha - 1, -1, -1):
                        if matriz[i][coluna] != 0:
                            multiplo = -1.0 * matriz[i][coluna]
                            if multiplo != 0:
                                linhaMaisOutraLinhaVezezMultiplo(
                                    i, linha, multiplo, matriz)

                print(mostrarMatrizEscalonada(
                    linhaMatriz, colunaMatriz, matriz))

                break

            elif matriz[linha][coluna] != 0:
                colunaPivoAnterior = coluna + 1

                if matriz[linha][coluna] != 1:
                    multiplo = matriz[linha][coluna]
                    linhaDivididoMultiplo(linha, multiplo, matriz)

                print(mostrarMatrizEscalonada(
                    linhaMatriz, colunaMatriz, matriz))

                for j in range(linha + 1, len(matriz)):
                    if matriz[j][coluna] != 0:
                        multiplo = -1.0 * matriz[j][coluna]
                        linhaMaisOutraLinhaVezezMultiplo(
                            j, linha, multiplo, matriz)
                print(mostrarMatrizEscalonada(
                    linhaMatriz, colunaMatriz, matriz))

                if (linha > 0):
                    for i in range(linha - 1, -1, -1):
                        if matriz[i][coluna] != 0:
                            multiplo = -1.0 * matriz[i][coluna]
                            if multiplo != 0:
                                linhaMaisOutraLinhaVezezMultiplo(
                                    i, linha, multiplo, matriz)
                    print(mostrarMatrizEscalonada(
                        linhaMatriz, colunaMatriz, matriz))
                break
    
def escalonamentoMatrizInversa(matriz):
    matriz = np.matrix(matriz, dtype=float)
    if np.linalg.det(matriz) != 0:
        print('Inversa por escalonamento')
        matrizIndentidade = np.zeros(shape=(len(matriz), len(matriz)))
        for i in range(0, len(matrizIndentidade)):
            for j in range(0, len(matrizIndentidade)):
                if(i == j):
                    matrizIndentidade[i, j] = 1

        print(mostrarMatriz(linhaMatriz, colunaMatriz,
              matriz.tolist(), matrizIndentidade.tolist()))


# Executa uma substituicao simples caso algum pivo da matriz original seja 0
        for i in range(0, len(matriz)):
            if(matriz[i, i] == 0 and matriz[i+1, i] != 0):
                mat = matriz[i, :].copy()
                matrizInv = matrizIndentidade[i, :].copy()
                matriz[i, :] = matriz[i+1, :]
                matrizIndentidade[i, :] = matrizIndentidade[i+1, :]
                matriz[i+1, :] = mat
                matrizIndentidade[i+1, :] = matrizInv
        print(mostrarMatriz(linhaMatriz, colunaMatriz,
              matriz.tolist(), matrizIndentidade.tolist()))


# Executa a eliminacao da parte inferior da matriz
        for i in range(1, len(matriz)):
            for j in range(0, len(matriz)-1):
                if(i != j):
                    if(matriz[i, j] != 0 and i > j):
                        matrizIndentidade[i, :] = matrizIndentidade[i, :] - \
                            matriz[i, j]*matrizIndentidade[j, :]/matriz[j, j]
                        matriz[i, :] = matriz[i, :] - \
                            matriz[i, j]*matriz[j, :]/matriz[j, j]

        print(mostrarMatriz(linhaMatriz, colunaMatriz,
              matriz.tolist(), matrizIndentidade.tolist()))

# Executa a operacao que deixa os pivos com valor de 1
        for i in range(0, len(matriz)):
            matrizIndentidade[i, :] = matrizIndentidade[i, :]/matriz[i, i]
            matriz[i, :] = matriz[i, :]/matriz[i, i]
        print(mostrarMatriz(linhaMatriz, colunaMatriz,
              matriz.tolist(), matrizIndentidade.tolist()))

# Executa a eliminacao para a parte superior do matriz
        for i in range(1, len(matriz)):
            for j in range(0, len(matriz)-1):
                if(i != j):
                    if(matriz[j, i] != 0):
                        matrizIndentidade[j, :] = matrizIndentidade[j,
                                                                    :] - matriz[j, i]*matrizIndentidade[i, :]/matriz[i, i]
                        matriz[j, :] = matriz[j, :] - \
                            matriz[j, i]*matriz[i, :]/matriz[i, i]

        print(mostrarMatriz(linhaMatriz, colunaMatriz,
              matriz.tolist(), matrizIndentidade.tolist()))

    else:
        print('Determinante é nulo')



linhaMatriz = int(input('Linhas: '))
colunaMatriz = int(input('Colunas: '))

matriz = []
matriz = matrizNula(linhaMatriz, colunaMatriz)


for l in range(linhaMatriz):
    for c in range(colunaMatriz):
        matriz[l][c] = int(
            input(f'Digite um valor para [{l + 1}, {c + 1}]: '))


if linhaMatriz == colunaMatriz:
    escalonamentoMatrizInversa(matriz)

else:
    if conferirMatrizNula(linhaMatriz, colunaMatriz, matriz):
       print('A matriz é nula') 
    else:
        print('\nEscalonamento de matriz: ')
        escalonarMatriz(matriz)
        


