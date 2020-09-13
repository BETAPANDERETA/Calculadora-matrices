#----------------------------------
#| Calculadora de MATRICES         |
#| AUTOR: BETAPANDERETA            |
#| Versión: 0.1.1                  |
#----------------------------------

from tabulate import tabulate

#----------------------------------
#       MATRICES DE ENTRADA        |
#----------------------------------
def crear_matriz(nom,fil,col):

    matriz = [] 

    for i in range(fil):
        fila = []
        matriz.append(fila)
        for j in range(col):
            column = int(input(nom+"["+str(i+1)+"]["+str(j+1)+"]:"))
            fila.append(column)
    
    return matriz

#----------------------------------
#       MATRIZ DE CEROS             |
#----------------------------------

def crear_matR(fil,colm):

    mat_R = []

    for i in range(fil):
        fila =[]
        mat_R.append(fila)
        for j in range (colm):
            colum=0
            fila.append(colum)
    
    return mat_R

#----------------------------------
#      IMPRIMIENDO MATRICES        |
#----------------------------------

def imp_matriz(matrix):

    print(tabulate(matrix,tablefmt="fancy_grid"))

#----------------------------------
#    OPERACIONES ENTRE MATRICES    |
#----------------------------------

def sumar_mat(
        coll,  # Colección de matrices que recibe 
        filas,  # Núm. Filas  de las matrices
        colm    # Núm. Columnas de las matrices
    ):
    
    mat_res = crear_matR(filas,colm)

    for k in range(filas):
        for l in range(colm):
            for m in range (len(coll)):
                mat_res[k][l] += coll[m][k][l]
    
    return mat_res

def mult_mat(
        coll, # Colección de matrices que recibe 
    ):

    matA = coll[0]
    matB = coll[1]
    mat_res = crear_matR(len(matA),len(matB[0]))

    c_A = len(matA[0]) # Columnas A
    f_B = len(matB)    # Filas B 

    # Operando las matrices

    if c_A == f_B:
        for k in range(len(mat_res)):
            for l in range(len(mat_res[k])):
                for j in range (len(mat_res)):
                    try:
                        mat_res[k][l] += matA[k][j]*matB[j][l]
                    except IndexError:
                        pass
    else:
        print("No definido")    

    return mat_res

#----------------------------------
#               MAIN              |
#----------------------------------

def main():

    coll_mat = [] # Colección de matrices

    while True:

        cant_mat =  int(input("Número de matrices: "))

        if cant_mat == 0:
            break

        for i in range(cant_mat): # Recibo n-matrices

            nom_mat = str(input("\nNombre matriz["+str(i+1)+"]:"))
            row = int(input("Filas: "))
            col = int(input("Columnas: "))
            print(tabulate([["MATRIZ",nom_mat]],tablefmt="fancy_grid"))

            matriz = crear_matriz(nom_mat,row,col)
            coll_mat.append(matriz)  #Guardando la matriz digitada en la colección de matrices
            imp_matriz(matriz)
        
        print(tabulate([["1","Sumar"],["2","Multiplicar"]],headers=["OPC","OPERACIÓN"],tablefmt="fancy_grid"))
        opc = int(input("SU OPCIÓN:"))
        print(tabulate([["MATRIZ","R"]],tablefmt="fancy_grid"))
        
        if opc == 1:
            imp_matriz(sumar_mat(coll_mat,row,col))
        if opc == 2 and cant_mat == 2:
            imp_matriz(mult_mat(coll_mat))

        coll_mat = [] # Limpiando la colección de matrices

        if opc == 0:
            break

if __name__ == '__main__':
    main()