class Revista:
# parameto constructor
    def __init__(self, categoria):
        self.categoria = categoria
    
   
    # Esta clase solo tiene el atributo categoría según el diagrama


# Paso 5: hacer obj -> Argumentos
revista1 = Revista("Tecnología")
revista2 = Revista("Deportes")
revista3 = Revista("Moda")
revista4 = Revista("Ciencia")

# mostrar datos
print("=== PROBANDO CLASE REVISTA ===")
print(f"Revista 1 - Categoría: {revista1.categoria}")
print(f"Revista 2 - Categoría: {revista2.categoria}")
print(f"Revista 3 - Categoría: {revista3.categoria}")
print(f"Revista 4 - Categoría: {revista4.categoria}")