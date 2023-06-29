from Libros import *
import random as rn
import numpy as np
##################
def ingresarLibro(lista_libros):
    obra = Libros()
    c = False
    while c == False:
        c = obra.setCodigo_libro(input("Ingrese codigo del libro:"))
    c = False
    while c == False:
        try:
            c = obra.setPrecio(int(input("Ingrese precio:")))
        except BaseException as error:
            print(f"error:{error}")
    c = False
    while c == False:
        try:
            c = obra.setApublicacion(int(input("Ingrese año de publicacion:")))
        except BaseException as error:
            print(f"error:{error}")
    obra.titulo=input("Ingrese titulo del libro:")
    obra.autor=input("Ingrese autor del libro:")
    obra.pais=input("Ingrese pais:")
    obra.categoria=input("Ingrese categoria:")
    return np.append(lista_libros, obra)
def buscarLibro(lista_libros):
    codigo = input("Ingrese codigo del libro:")
    flag=False
    for libros in lista_libros:
        if codigo == libros.codigo_libro:
            flag = True
            print(f"codigo del libros:{libros.codigo_libro:}")
            print(f"Titulo libro:{libros.titulo}")
            print(f"autor:{libros.autor}")
            if (2023-libros.a_publicacion) > 5:
                libros.precio=libros.precio*0.85
            print(f"precio:{int(libros.precio)}")
            print(f"pais:{libros.pais}")
            print(f"categoria:{libros.categoria}")
            if (2023-libros.a_publicacion) > 30:
                print(f"Libro edicion especial,año de publicacion:{libros.a_publicacion}")
            else:
                print(f"Año de publicacion:{libros.a_publicacion}")
            break
    if flag == False:
        print("Libro no encontrado")
def imprimirPais(lista_libros):
    informe = rn.randint(1500, 5000)
    pais = input("Ingrese pais:")
    flag = False
    print("Listado por pais")
    print(f"Numero de Informe:{informe}")
    for libros in lista_libros:
        if pais == libros.pais:
            flag=True
            print(f"Titulo Libro:{libros.titulo}")
            if (2023-libros.a_publicacion) > 5:
                libros.precio=libros.precio*0.85
            print(f"Precio:{int(libros.precio)}")
            print(f"Categoria:{libros.categoria}")
            print(f"Autor:{libros.autor}")
    if flag == False:
        print("Pais no encontrado")
def imprimirCategoria(lista_libros):
    informe = rn.randint(1500, 5000)
    categoria = input("Ingrese categoria:")
    flag = False
    print("Listado por categoria")
    print(f"Numero de Informe:{informe}")
    for libros in lista_libros:
        if categoria == libros.categoria:
            flag = True
            print(f"Titulo Libro:{libros.titulo}")
            if (2023-libros.a_publicacion) > 5:
                libros.precio=libros.precio*0.85
            print(f"Precio:{int(libros.precio)}")
            print(f"Categoria:{libros.categoria}")
            print(f"Autor:{libros.autor}")
    if flag == False:
        print("Pais no encontrado")
def listadoInformes(lista_libros):
    print("Imprimir Informes")
    print("1) Imprimir por Pais")
    print("2) Imprimir por categoria")
    try:
        op_informe=int(input("Seleccione(1-2):"))
        match op_informe:
            case 1:
                imprimirPais(lista_libros)
            case 2:
                imprimirCategoria(lista_libros)
            case _:
                print("Opcion incorrecta")
    except BaseException as error:
        print(f"error:{error}")
def salir():
    print("Autor:Gonzalo Aliaga, Hasta pronto")
    return False
##################
lista_libros = np.array([])
ciclo = True
while ciclo:
    print("Libreria Mayor")
    print("1) Grabar Libro")
    print("2) Buscar Libro")
    print("3) Imprimir Informes")
    print("4) Salir")
    try:
        op = int(input("Seleccione (1-4):"))
        match op:
            case 1:
                lista_libros=ingresarLibro(lista_libros)
            case 2:
                buscarLibro(lista_libros)
            case 3:
                listadoInformes(lista_libros)
            case 4:
                ciclo=salir()
            case _:
                print("Opcion incorrecta")
    except BaseException as error:
        print(f"error:{error}")