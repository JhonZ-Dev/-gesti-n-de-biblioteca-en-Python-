class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

class Biblioteca:
    def __init__(self):
        self.libros = []
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
        
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")
    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                print(f"Libro encontrado - Título: {libro.titulo}, Autor: {libro.autor}, ISBN: {libro.isbn}")
                return
        print(f"Libro con el título '{titulo}' no encontrado en la biblioteca.")
    def mostrar_libros(self):
        print("Lista de libros en la biblioteca:")
        for libro in self.libros:
            print(f"Título: {libro.titulo}, Autor: {libro.autor}, ISBN: {libro.isbn}")