# Tarea 1 - Taller de Python para Ciencias de Datos
# Autores: Cristofer Alarcón, Felipe Espinoza, Francisco Salazar
# Descripción del proyecto:
# Este es un programa de lectura de archivos de texto con una codificación UTF-8. 
# El programa tiene las siguientes funcionalidades:
# · Se puede obtener una estadística del documento seleccionado.
# · Buscar una palabra en el documento y mostrar cuántas veces se repite.
# · Reemplazar una palabra en el documento.

def opcion_1(nombre_libro):

    libro = open(nombre_libro, "rt", encoding="UTF-8")

    # Se retorna el puntero al inicio del archivo.
    libro.seek(0)

    # Cantidad total de líneas
    variable = len(libro.readlines())+1
    print("Cantidad total de líneas:", variable)

    # Cantidad total de palabras
    libro.seek(0)
    data = libro.read()
    palabras = data.split()
    print("Cantidad total de palabras:", len(palabras))

    # Palabras no repetidas
    libro.seek(0)
    f = open(nombre_libro, 'r', encoding="utf-8")
    data = f.read()
    f1 = data.replace(":", "")
    f1 = f1.replace(",", "")

    palabras = f1.split()
    diccionario = dict()

    for p in palabras:
        diccionario[p] = diccionario.get(p, 0) + 1
    count = 0
    for key in diccionario:
        if diccionario[key] == 1:
            count = count + 1
    print("Número de palabras no repetidas:", count)

    # Cantidad de caracteres con espacio.
    print("Cantidad de caracteres con espacio:", len(data))

    # Cantidad de caracteres sin espacio.
    libro.seek(0)
    leer = libro.read()
    sin_espacio = len(leer) - leer.count(' ')
    print("Cantidad de caracteres sin espacio:", sin_espacio)
    print("\n")

def opcion_2(nombre_libro):
    libro = open(nombre_libro, "rt", encoding="UTF-8")

    # Se retorna el puntero al inicio del archivo.
    libro.seek(0)

    # Revisa si la palabra esta en el texto. Si existe, la imprime.
    leer = libro.read()
    palabra = input("Ingrese la palabra a buscar: ")
    if palabra in leer:
        print("La palabra '"+palabra+"' se encuentra",
              leer.count(palabra), "veces en el texto.\n")
    else:
        print("La palabra '"+palabra+"' no está en el texto.\n")

def opcion_3(nombre_libro):
    libro = open(nombre_libro, "rt", encoding="UTF-8")

    # Se retorna el puntero al inicio del archivo
    libro.seek(0)

    print("Ingrese la palabra a reemplazar: ")
    palabra_buscar = input()

    print("Ingrese la palabra que reemplazará a '"+palabra_buscar+"'.")
    palabra_reemplazar = input()

    print("Se reemplazó la palabra '"+palabra_buscar +
          "' por la palabra '"+palabra_reemplazar+"'.\n")

    with open(nombre_libro, 'r') as file:
        filedata = file.read()
        filedata = filedata.replace(palabra_buscar, palabra_reemplazar)
    with open(nombre_libro, 'w') as file:
        file.write(filedata)

def numero():

    num = 0
    ingreso = False

    while(not ingreso):
        try:
            num = int(input("Ingrese la opción que desee: "))
            if num >= 1 & num <= 7:
                ingreso = True
            else:
                print('Error, introduce una opción válida.')
        except ValueError:
            print('Error, ingrese un número natural.')

    return num

salir = False
opcion = 0

while not salir:

    print("Elige una opción")
    print("------------------------------------")
    print("1. El árbol de la colina")
    print("2. El caos reptante")
    print("3. En el mar remoto")
    print("4. Lazarillo de Tormes")
    print("5. Para leer al atardecer")
    print("6. Una corta historia del eBook")
    print("7. Salir")
    print("------------------------------------")

    opcion = numero()

    if opcion == 1:
        volver = False
        opcion = 0
        nombre_libro = "Libros_txt_utf-8/El_Arbol_De_La_Colina.txt"
        while not volver:
            print("Se seleccionó el libro 'El árbol de la colina'.")
            print("---------------------------------------------------------------------")
            print("1. Entregar las estadísticas del documento")
            print("2. Buscar una palabra en el documento y las veces que esta repetida")
            print("3. Reemplazar una palabra en el texto.")
            print("4. Volver al menú.")
            print("---------------------------------------------------------------------")
            print("Elige una opcion\n")

            opcion = numero()
            if opcion == 1:
                print("1. Entregar las estadísticas del documento: \n")
                opcion_1(nombre_libro)
            elif opcion == 2:
                print(
                    "2. Buscar una palabra en el documento y las veces que esta repetida:\n ")
                opcion_2(nombre_libro)
            elif opcion == 3:
                print("3. Reemplazar una palabra en el texto: \n")
                opcion_3(nombre_libro)
            elif opcion == 4:
                volver = True
            else:
                print("Ingrese una opción válida.\n")

    elif opcion == 2:
        volver = False
        opcion = 0
        nombre_libro = "Libros_txt_utf-8/El_Caos_Reptante.txt"
        while not volver:
            print("Se seleccionó el libro 'El caos reptante'.")
            print("---------------------------------------------------------------------")
            print("1. Entregar las estadísticas del documento")
            print("2. Buscar una palabra en el documento y las veces que esta repetida")
            print("3. Reemplazar una palabra en el texto.")
            print("4. Volver al menú.")
            print("---------------------------------------------------------------------")
            print("Elige una opcion\n")

            opcion = numero()
            if opcion == 1:
                print("1. Entregar las estadísticas del documento: \n")
                opcion_1(nombre_libro)
            elif opcion == 2:
                print(
                    "2. Buscar una palabra en el documento y las veces que esta repetida:\n ")
                opcion_2(nombre_libro)
            elif opcion == 3:
                print("3. Reemplazar una palabra en el texto: \n")
                opcion_3(nombre_libro)
            elif opcion == 4:
                volver = True
            else:
                print ("Ingrese una opción válida.\n")

    elif opcion == 3:
        volver = False
        opcion = 0
        nombre_libro = "Libros_txt_utf-8/En_El_Mar_Remoto.txt"
        while not volver:
            print("Se seleccionó el libro 'En el mar remoto'.")
            print("---------------------------------------------------------------------")
            print("1. Entregar las estadísticas del documento")
            print("2. Buscar una palabra en el documento y las veces que esta repetida")
            print("3. Reemplazar una palabra en el texto.")
            print("4. Volver al menú.")
            print("---------------------------------------------------------------------")
            print("Elige una opcion\n")

            opcion = numero()
            if opcion == 1:
                print("1. Entregar las estadísticas del documento: \n")
                opcion_1(nombre_libro)
            elif opcion == 2:
                print(
                    "2. Buscar una palabra en el documento y las veces que esta repetida:\n ")
                opcion_2(nombre_libro)
            elif opcion == 3:
                print("3. Reemplazar una palabra en el texto: \n")
                opcion_3(nombre_libro)
            elif opcion == 4:
                volver = True
            else:
                print ("Ingrese una opción válida.\n")

    elif opcion == 4:
        volver = False
        opcion = 0
        nombre_libro = "Libros_txt_utf-8/Lazarillo_de_Tormes.txt"
        while not volver:
            print("Se seleccionó el libro 'Lazarillo de Tormes'")
            print("---------------------------------------------------------------------")
            print("1. Entregar las estadísticas del documento")
            print("2. Buscar una palabra en el documento y las veces que esta repetida")
            print("3. Reemplazar una palabra en el texto.")
            print("4. Volver al menú.")
            print("---------------------------------------------------------------------")
            print("Elige una opcion\n")

            opcion = numero()
            if opcion == 1:
                print("1. Entregar las estadísticas del documento: \n")
                opcion_1(nombre_libro)
            elif opcion == 2:
                print(
                    "2. Buscar una palabra en el documento y las veces que esta repetida:\n ")
                opcion_2(nombre_libro)
            elif opcion == 3:
                print("3. Reemplazar una palabra en el texto: \n")
                opcion_3(nombre_libro)
            elif opcion == 4:
                volver = True
            else:
                print ("Ingrese una opción válida.\n")

    elif opcion == 5:
        volver = False
        opcion = 0
        nombre_libro = "Libros_txt_utf-8/Para_Leer_Al_Atardecer.txt"
        while not volver:
            print("Se seleccionó el libro 'Para leer al atardecer'")
            print("---------------------------------------------------------------------")
            print("1. Entregar las estadísticas del documento")
            print("2. Buscar una palabra en el documento y las veces que esta repetida")
            print("3. Reemplazar una palabra en el texto.")
            print("4. Volver al menú.")
            print("---------------------------------------------------------------------")
            print("Elige una opcion\n")

            opcion = numero()
            if opcion == 1:
                print("1. Entregar las estadísticas del documento: \n")
                opcion_1(nombre_libro)
            elif opcion == 2:
                print(
                    "2. Buscar una palabra en el documento y las veces que esta repetida:\n ")
                opcion_2(nombre_libro)
            elif opcion == 3:
                print("3. Reemplazar una palabra en el texto: \n")
                opcion_3(nombre_libro)
            elif opcion == 4:
                volver = True
            else:
                print("Ingrese una opción válida.\n")

    elif opcion == 6:
        volver = False
        opcion = 0
        nombre_libro = "Libros_txt_utf-8/Una_corta_historia_del_eBook.txt"
        while not volver:
            print("Se seleccionó el libro 'Una corta historia del eBook'.")
            print("---------------------------------------------------------------------")
            print("1. Entregar las estadísticas del documento")
            print("2. Buscar una palabra en el documento y las veces que esta repetida")
            print("3. Reemplazar una palabra en el texto.")
            print("4. Volver al menú.")
            print("---------------------------------------------------------------------")
            print("Elige una opcion\n")

            opcion = numero()
            if opcion == 1:
                print("1. Entregar las estadísticas del documento: \n")
                opcion_1(nombre_libro)
            elif opcion == 2:
                print(
                    "2. Buscar una palabra en el documento y las veces que esta repetida:\n ")
                opcion_2(nombre_libro)
            elif opcion == 3:
                print("3. Reemplazar una palabra en el texto: \n")
                opcion_3(nombre_libro)
            elif opcion == 4:
                volver = True
            else:
                print("Ingrese una opción válida.\n")

    elif opcion == 7:
        salir = True
        print("Fin")

    else:
        print("Ingrese una opción válida.\n")
