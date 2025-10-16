class Libro:
    def __init__(self, titulo, autor, categoria):
        self._titulo = titulo
        self._autor = autor
        self._categoria = categoria
        self._disponible = True

    def get_titulo(self):
        return self._titulo

    def get_autor(self):
        return self._autor

    def get_categoria(self):
        return self._categoria

    def esta_disponible(self):
        return self._disponible

    def prestar(self):
        if self._disponible:
            self._disponible = False
            return True
        return False

    def devolver(self):
        self._disponible = True

    def __str__(self):
        estado = "Disponible" if self._disponible else "Prestado"
        return f"{self._titulo} - {self._autor} ({self._categoria}) - {estado}"


class Usuario:
    def __init__(self, nombre, codigo):
        self._nombre = nombre
        self._codigo = codigo
        self._prestamos = []

    def get_nombre(self):
        return self._nombre

    def get_codigo(self):
        return self._codigo

    def prestar_libro(self, libro: Libro):
        if libro.prestar():
            self._prestamos.append(libro)
            print(f"{self._nombre} ha prestado el libro: {libro.get_titulo()}")
            return True
        else:
            print(f"El libro {libro.get_titulo()} no está disponible.")
            return False

    def devolver_libro(self, libro: Libro):
        if libro in self._prestamos:
            libro.devolver()
            self._prestamos.remove(libro)
            print(f"{self._nombre} devolvió el libro: {libro.get_titulo()}")
            return True
        else:
            print(f"{self._nombre} no tiene prestado el libro {libro.get_titulo()}")
            return False

    def __str__(self):
        return f"Usuario: {self._nombre} (Código: {self._codigo})"


class BibliotecaViewModel:
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def registrar_libro(self, titulo, autor, categoria):
        self.biblioteca._libros.append(Libro(titulo, autor, categoria))
        return f"Libro '{titulo}' registrado correctamente."

    def registrar_usuario(self, nombre, codigo):
        self.biblioteca._usuarios.append(Usuario(nombre, codigo))
        return f"Usuario '{nombre}' registrado correctamente."

    def prestar_libro(self, codigo, titulo):
        usuario = self.biblioteca.buscar_usuario(codigo)
        libro = self.biblioteca.buscar_libro(titulo)
        if usuario and libro:
            success = usuario.prestar_libro(libro)
            if success:
                return "Préstamo realizado con éxito."
            else:
                return "No se pudo realizar el préstamo (el libro no está disponible)."
        return "Usuario o libro no encontrado."

    def devolver_libro(self, codigo, titulo):
        usuario = self.biblioteca.buscar_usuario(codigo)
        libro = self.biblioteca.buscar_libro(titulo)
        if usuario and libro:
            success = usuario.devolver_libro(libro)
            if success:
                return "Devolución realizada con éxito."
            else:
                return "El usuario no tiene prestado ese libro."
        return "Usuario o libro no encontrado."


class Biblioteca:
    def __init__(self, nombre):
        self._nombre = nombre
        self._libros = []
        self._usuarios = []
        self.viewmodel = BibliotecaViewModel(self)

    def buscar_libro(self, titulo):
        for libro in self._libros:
            if libro.get_titulo().lower() == titulo.lower():
                return libro
        return None

    def buscar_usuario(self, codigo):
        for usuario in self._usuarios:
            if usuario.get_codigo() == codigo:
                return usuario
        return None

    def mostrar_libros(self):
        print("\nCatálogo de libros:")
        if not self._libros:
            print("No hay libros registrados.")
            return
        for libro in self._libros:
            print(libro)

    def mostrar_usuarios(self):
        print("\nLista de usuarios:")
        if not self._usuarios:
            print("No hay usuarios registrados.")
            return
        for usuario in self._usuarios:
            print(usuario)

    def mostrar_menu(self):
        while True:
            print(f"\n {self._nombre} ")
            print("1. Registrar libro")
            print("2. Registrar usuario")
            print("3. Mostrar catálogo de libros")
            print("4. Mostrar lista de usuarios")
            print("5. Prestar libro")
            print("6. Devolver libro")
            print("7. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                titulo = input("Título del libro: ")
                autor = input("Autor del libro: ")
                categoria = input("Categoría del libro: ")
                print(self.viewmodel.registrar_libro(titulo, autor, categoria))
                self.mostrar_libros()

            elif opcion == "2":
                nombre = input("Nombre del usuario: ")
                codigo = input("Código del usuario: ")
                print(self.viewmodel.registrar_usuario(nombre, codigo))
                self.mostrar_usuarios()

            elif opcion == "3":
                self.mostrar_libros()

            elif opcion == "4":
                self.mostrar_usuarios()

            elif opcion == "5":
                codigo = input("Código del usuario: ")
                titulo = input("Título del libro a prestar: ")
                print(self.viewmodel.prestar_libro(codigo, titulo))
                self.mostrar_libros()

            elif opcion == "6":
                codigo = input("Código del usuario: ")
                titulo = input("Título del libro a devolver: ")
                print(self.viewmodel.devolver_libro(codigo, titulo))
                self.mostrar_libros()

            elif opcion == "7":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    biblioteca = Biblioteca("Biblioteca UNAL")
    biblioteca.mostrar_menu()

