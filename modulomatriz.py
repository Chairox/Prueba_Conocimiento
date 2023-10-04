import tkinter as tk
def proyectoMatriz():
    def impmatriz(matriz, filaseleccion, columnaseleccion):
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if i == filaseleccion or j == columnaseleccion:
                    print((matriz[i][j]), end="\t")
                else:
                    print(matriz[i][j], end="\t")
            print()
    def deshabilitarpunto(matriz, fila, columna):
        for i in range(len(matriz)):
            matriz[i][columna] = 'X'
        for j in range(len(matriz[0])):
            matriz[fila][j] = 'X'
    def clickpunto(fila, columna):
        if (fila, columna) not in seleccionpunto:
            seleccionpunto.append((fila, columna))
            if len(seleccionpunto) <= 5:
                valor = matriz[fila][columna]
                print(f"""Seleccionó el punto {valor} en la fila {fila+1} y columna {columna+1}
        Los puntos totales seleccionados son: {seleccionpunto}""")
                deshabilitarpunto(matriz, fila, columna)
                impmatriz(matriz, -1, -1)
            else:
                print("Solo puede seleccionar 5 puntos")
        else:
            print(f"El punto {valor} ya ha sido seleccionado, intente otro valor")
    def botones(root, texto, fila, columna):
        boton = tk.Button(root, text=texto, command=lambda: clickpunto(fila, columna))
        boton.grid(row=fila, column=columna)

    matriz = [[i*5 + j + 1 for j in range(5)] for i in range(10)]

    seleccionpunto = []

    root = tk.Tk()
    root.title("Matriz Proyecto")

    for i in range(10):
        for j in range(5):
            texto = matriz[i][j]
            botones(root, texto, i, j)

    root.mainloop()
