class Email:
    __idCuenta = ''
    __dominio  = ''
    __tipoDominio = ''
    __password = '1234'

    def __init__(self,correo,idCuenta='',dominio='',tipoDominio=''):
        if(correo == ''):
            self.__password = '1234'
            self.__idCuenta = idCuenta
            self.__dominio = dominio
            self.__tipoDominio = tipoDominio
        else:
            self.crearCuenta(correo)


    def getDominio(self):
        return self.__dominio

    def informacionCuenta(self):
        print("\n\tInformacion de la cuenta\n\tmail: {}\n\tdominio: {}\n\ttipoDominio: {}.".format(self.__idCuenta,self.__dominio,self.__tipoDominio))

    def retornaEmail(self):
        return self.__idCuenta + "@" + self.__dominio + self.__tipoDominio

    def modificarPassword(self):
        while True:
            password = input("Ingrese la contrasenia actual: ")
            if(password == self.__password):
                nuevo = input("Ingrese la nueva contrasenia: ")
                self.__password = nuevo
                print("Contrasenia cambiada con exito")
                break
            else:
                print("Contrasenia invalida, vuelva a intentar")

    def crearCuenta(self, correo):
        nombre = correo.split('@')
        self.__idCuenta = nombre[0]
        self.__dominio = nombre[1].split('.')[0]
        self.__tipoDominio = "." + nombre[1].split('.')[1]
        print("\tCuenta creada con exito")
        self.informacionCuenta()
        self.retornaEmail()