class Hilo:
    def busca_novedades_metodo(self, categoria):
        print(f"Buscando novedades en la categoría: {categoria}")
        return f"Novedades encontradas en '{categoria}'"


# Paso 5: hacer obj
hilo = Hilo()

# Paso 6: llamar Métodos -> Argumento -> E.D
print("=== PROBANDO CLASE HILO ===")
print(hilo.busca_novedades_metodo("Libros"))
print(hilo.busca_novedades_metodo("Revistas"))
print(hilo.busca_novedades_metodo("Artículos"))