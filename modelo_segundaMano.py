class ArticuloSegundaMano:

    
    # metodo Constructor con parametros
    def __init__(self, clasificacion, tema, vendedor):
        self.clasificacion = clasificacion
        self.tema = tema
        self.vendedor = vendedor
    
    # Metodos Normales
    # Esta clase solo tiene atributos según el diagrama


#  hacer obj -> Argumentos
articulo1 = ArticuloSegundaMano("Libro Usado", "Programación", "Juan Pérez")
articulo2 = ArticuloSegundaMano("Revista Usada", "Historia", "María López")
articulo3 = ArticuloSegundaMano("Libro Seminuevo", "Matemáticas", "Carlos Ruiz")

#  Mostrar datos
print("=== PROBANDO CLASE ARTÍCULO DE SEGUNDA MANO ===")
print(f"Artículo 1 - Clasificación: {articulo1.clasificacion}, Tema: {articulo1.tema}, Vendedor: {articulo1.vendedor}")
print(f"Artículo 2 - Clasificación: {articulo2.clasificacion}, Tema: {articulo2.tema}, Vendedor: {articulo2.vendedor}")
print(f"Artículo 3 - Clasificación: {articulo3.clasificacion}, Tema: {articulo3.tema}, Vendedor: {articulo3.vendedor}")