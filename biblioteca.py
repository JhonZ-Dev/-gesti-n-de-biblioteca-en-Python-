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
# Ejemplo de uso
if __name__ == "__main__":
    # Crear algunos libros
    libro1 = Libro("Python Crash Course", "Eric Matthes", "9781593279288")
    libro2 = Libro("Clean Code", "Robert C. Martin", "9780132350884")
    libro3 = Libro("The Pragmatic Programmer", "Andrew Hunt, David Thomas", "9780201616224")

    # Crear una biblioteca
    biblioteca = Biblioteca()

    # Agregar libros a la biblioteca
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    # Mostrar la lista de libros en la biblioteca
    biblioteca.mostrar_libros()

    # Buscar un libro por título
    biblioteca.buscar_libro("Clean Code")
    biblioteca.buscar_libro("Learning Python")