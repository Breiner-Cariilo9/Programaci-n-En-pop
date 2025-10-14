class Libro:
 # Constructor con parametros
    def __init__(self, genero):
        self.genero = genero
    
    # metodos Normales
    # Esta clase solo tiene el atributo genero según el diagrama


#  hacer obj -> Argumentos
libro1 = Libro("Ficción")
libro2 = Libro("Ciencia Ficción")
libro3 = Libro("Romance")
libro4 = Libro("Terror")

# Mostrar datos
print("=== PROBANDO CLASE LIBRO ===")
print(f"Libro 1 - Género: {libro1.genero}")
print(f"Libro 2 - Género: {libro2.genero}")
print(f"Libro 3 - Género: {libro3.genero}")
print(f"Libro 4 - Género: {libro4.genero}")