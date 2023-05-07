from email import Email
from leerArchivo import archivoEmail

if __name__ == '__main__':

    #punto 1
    nombre = "Janet"
    e = Email("",'janetgtores','gmail','.com')
    print("\n\tEstimada {} te enviaremos tus mensajes a la dirección {}.".format(nombre, e.retornaEmail()))

    #punto2
    #contraseña por defecto: 1234
    e.modificarPassword()

    #punto 3
    email1 = Email("informatica.fcefn@gmail.com")

    #punto 4
    #archivo = open('direcciones','r')
    #reader = csv.reader(archivo, delimiter=',')
    nuevo = archivoEmail("direcciones.txt")
    nuevo.getCantDominios()