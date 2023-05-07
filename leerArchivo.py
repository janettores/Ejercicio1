from email import Email

class archivoEmail:
    def __init__(self,nombre):
        self.__archivo = open(nombre, 'r')
        self.__correos = self.__archivo.read().split(',')
        self.__email = []
        for correo in self.__correos:
            self.__email.append(Email(correo))

    def prueba(self,dominio,n):
        contador = 0
        for e in self.__email:
            if (e.getDominio() == dominio):
                contador = contador + 1
        if(contador == n):
            print("Se obtuvieron los resultados deseados")
        else:
            print("No se obtuvieron los resultados deseados")
    def getCantDominios(self):
        dominio = input("\n\tIngresar dominio: ")
        contador = 0
        for e in self.__email:
            if (e.getDominio() == dominio):
                contador = contador + 1
        print("Hay {} correos con el dominio {}.".format(contador, dominio))
