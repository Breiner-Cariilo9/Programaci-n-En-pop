class Producto:
#metodo Constructor con parámetros
    def __init__(self, precio, titulo, autor, editorial, anio_de_edicion):
        self.precio = precio
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.anio_de_edicion = anio_de_edicion
        self.preferencias = []
    
    #mtodos Normales
    def vender(self):
        print(f"Vendiendo producto: {self.titulo}")
        return f"Producto '{self.titulo}' vendido por ${self.precio}"
    
    def comprar(self):
        print(f"Comprando producto: {self.titulo}")
        return f"Producto '{self.titulo}' comprado"
    
    def ver_catalogo(self):
        print(f"Mostrando catálogo del producto {self.titulo}")
        return f"Título: {self.titulo}, Autor: {self.autor}, Editorial: {self.editorial}, Año: {self.anio_de_edicion}, Precio: ${self.precio}"


#hacer obj -> Argumentos
producto1 = Producto(45.99, "Cien Años de Soledad", "Gabriel García Márquez", "Sudamericana", 1967)
producto2 = Producto(35.50, "Don Quijote de la Mancha", "Miguel de Cervantes", "Planeta", 1605)
producto3 = Producto(28.00, "El Principito", "Antoine de Saint-Exupéry", "Salamandra", 1943)

# llamar Métodos -> Argumento -> E.D
print("=== PROBANDO CLASE PRODUCTO ===")
print(producto1.ver_catalogo())
print(producto1.vender())
print(producto1.comprar())
print("\n--- Producto 2 ---")
print(producto2.ver_catalogo())
print("\n--- Producto 3 ---")
print(producto3.ver_catalogo())