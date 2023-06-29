class Libros:
    codigo_libro=''
    titulo=''
    autor=''
    precio=0
    pais=''
    categoria=''
    a_publicacion=0

    def __int__(self):
        self.codigo_libro='AAA-111'
        self.titulo='S/T'
        self.autor='S/A'
        self.precio=10000
        self.pais='S/P'
        self.categoria='S/C'
        self.a_publicacion=2023

    def setCodigo_libro(self,codigo):
        if len(codigo) == 7:
            if codigo[0:3].isalpha() and codigo[3:4] == '-' and codigo[4:7].isdigit():
                self.codigo_libro = codigo
                return True
            else:
                print("Formato no valid Ej. AAC-123")
                return False
        else:
            print("Largo incorrecto")
            return False

    def setPrecio(self,precio):
        if precio >= 10000 and precio <= 150000:
            self.precio = precio
            return True
        else:
            print("Precio incorrecto, debe estar entre 10000 y 150000")
            return False

    def setApublicacion(self,apublicacion):
        if apublicacion >= 1780 and apublicacion <= 2023:
            self.a_publicacion = apublicacion
            return True
        else:
            print("Año de publicacion incorrecto, debe estar entre 1780 y 2023")
            return False

