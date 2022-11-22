Guardar_Libros = []
class Usuario:

    def __init__(self):
        self.Nombre = " "
        self.Telefono = " "
        self.CC = " "
    
    def Datos(self):
        self.Nombre = input("Digite su nombre: ")
        self.CC = int(input("Digite su cedula: "))
        self.Telefono = int(input("Digite su telefono: "))

class Persona:
    
    def __init__(self) -> None:
        self.Autor = " "
    
    def GetAutor(self):
        return self.Autor
    
    def SetAutor(self,autor):
        self.Autor = autor

class Lugar:

    def __init__(self) -> None:
        self.Lugar = " "
    
    def GetLugar(self):
        return self.Lugar
    
    def SetLugar(self,lugar):
        self.Lugar = lugar

class Fecha:
    
    def __init__(self) -> None:
        self.Fecha = " "
    
    def GetFecha(self):
        return self.Fecha
    
    def SetFecha(self,fecha):
        self.Fecha = fecha

class Prestar(Usuario, Persona, Lugar, Fecha):

    def __init__(self):
        self.Cantidad = 0
        self.Libro = " "
        self.ISBN = " "
        self.Paginas = " "
        self.Edicion = " "
        self.Editorial = " "
        super().__init__()

    def Prestando (self):
        print("Bienvenido a la biblioteca San Benito, ",self.Nombre)
        self.Cantidad = int(input("Digite la cantidad de libros que desea leer: "))
        for s in range(self.Cantidad):
            print("~~~~Libro ",s," ~~~~")
            self.Libro = input("Nombre del libro: ")
            self.ISBN = input("ISBN del libro: ")
            self.Paginas = int(input("Paginas del libro: "))
            self.Edicion = input("Edicion del libro que desea tener: ")
            self.Editorial = input("Digite el editorial: ")
            self.SetAutor(input("Nombre del autor: "))
            self.SetLugar(input("Digite el lugar del libro: "))
            self.SetFecha(input("Fecha de lanzamiento del libro: "))
            Nuevo = (self.Libro, self.ISBN, self.Paginas, self.Edicion, self.Editorial,self.Autor,self.Lugar,self.Fecha)
            Guardar_Libros.append(Nuevo)
    
class Libro(Prestar,Persona, Lugar, Fecha):

    def __init__(self):
        super().__init__()
        super().Datos()
        super().Prestando()
        self.MostrarResultado()

    def MostrarResultado (self):
        for s in range (self.Cantidad):
            print("Lista de libros que adquiri0: ")
            print("------- Libro ",s," ------")
            print("  _____________________________________________________")
            print(" | Titulo: ",Guardar_Libros[s][0])
            print("S|",Guardar_Libros[s][3])
            print(" | Autor: ",Guardar_Libros[s][5])
            print(" | ISBN: ",Guardar_Libros[s][1])
            print("S|",Guardar_Libros[s][4],",", Guardar_Libros[s][6],",", Guardar_Libros[s][7])
            print(" |",Guardar_Libros[s][2]," Paginas")
            print("  _____________________________________________________")

Librito  = Libro()