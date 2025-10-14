class Novedades:
#metodo Constructor con parámetros
    def __init__(self, clasificacion, tema):
        self.clasificacion = clasificacion
        self.tema = tema
    
    # funciones normales
    def cambiar_clasificacion(self, nueva_clasificacion):
        print(f"Cambiando clasificación de '{self.clasificacion}' a '{nueva_clasificacion}'")
        self.clasificacion = nueva_clasificacion
        return f"Clasificación actualizada a: {self.clasificacion}"


#obj -> Argumentos
novedad1 = Novedades("Nuevo Lanzamiento", "Ciencia Ficción")
novedad2 = Novedades("Best Seller", "Thriller")
novedad3 = Novedades("Recomendado", "Autoayuda")

#llamar Métodos -> Argumento -> E.D
print("=== PROBANDO CLASE NOVEDADES ===")
print(f"Novedad 1 - Clasificación: {novedad1.clasificacion}, Tema: {novedad1.tema}")
print(novedad1.cambiar_clasificacion("Top Ventas"))
print(f"Novedad 1 actualizada - Clasificación: {novedad1.clasificacion}")
print(f"\nNovedad 2 - Clasificación: {novedad2.clasificacion}, Tema: {novedad2.tema}")
print(novedad2.cambiar_clasificacion("Más Vendido"))