class ArticuloOnline:
 #metodo Constructor con parámetros
    def __init__(self, tema):
        self.tema = tema
    
    # Paso 4: Métodos Normales
    def publicar(self):
        print(f"Publicando artículo online sobre: {self.tema}")
        return f"Artículo '{self.tema}' publicado exitosamente"


#hacer obj -> Argumentos
articulo_online1 = ArticuloOnline("Inteligencia Artificial")
articulo_online2 = ArticuloOnline("Desarrollo Web")
articulo_online3 = ArticuloOnline("Machine Learning")

#llamar Métodos -> Argumento -> E.D
print("=== PROBANDO CLASE ARTÍCULO ONLINE ===")
print(articulo_online1.publicar())
print(articulo_online2.publicar())
print(articulo_online3.publicar())