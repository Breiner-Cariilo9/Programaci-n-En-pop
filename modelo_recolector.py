class Recolector:
    
    #metodos Normales
    def envia_novedades_metodo(self, lista_novedades):
        print(f"Enviando {len(lista_novedades)} novedades...")
        for novedad in lista_novedades:
            print(f"  - {novedad}")
        return f"{len(lista_novedades)} novedades enviadas"


# Paso 5: hacer obj
recolector = Recolector()

# Paso 6: llamar Métodos -> Argumento -> E.D
print("=== PROBANDO CLASE RECOLECTOR ===")
novedades = ["Nuevo libro de programación", "Revista tecnológica edición especial", "Bestseller del mes"]
print(recolector.envia_novedades_metodo(novedades))