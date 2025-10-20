class Indexador:
    def actualiza_almacen_metodo(self):
        print("Actualizando almacén...")
        return "Almacén actualizado correctamente"
    
    def envia_resultado_busquedan_metodo(self, termino_busqueda):
        print(f"Enviando resultados de búsqueda para: {termino_busqueda}")
        return f"Resultados encontrados para '{termino_busqueda}'"


# hacer obj
indexador = Indexador()

# llamar Métodos
print("=== PROBANDO CLASE INDEXADOR ===")
print(indexador.actualiza_almacen_metodo())
print(indexador.envia_resultado_busquedan_metodo("libro python"))
print(indexador.envia_resultado_busquedan_metodo("revista tecnología"))