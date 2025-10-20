#codigo principal

from modelo_usuario import Usuario
from modelo_producto import Producto
from modelo_libro import Libro
from modelo_revista import Revista
from modelo_segundaMano import ArticuloSegundaMano
from modelo_novedades import Novedades
from modelo_Aonline import ArticuloOnline
from modelo_hilo import Hilo
from modelo_editorial import Editorial
from modelo_recolector import Recolector
from modelo_servidor import Servidor
from modelo_indexador import Indexador
from modelo_procesador import Procesador

#obj usuario
usuario1 = Usuario("Juan", "Pérez", "12345", "Calle 123", "juan123", "pass123")
usuario2 = Usuario("María", "López", "67890", "Av. Principal", "maria456", "pass456")

#obj producto 
producto1 = Producto(45.99, "Cien Años de Soledad", "Gabriel García Márquez", "Sudamericana", 1967)
producto2 = Producto(35.50, "Don Quijote de la Mancha", "Miguel de Cervantes", "Planeta", 1605)
producto3 = Producto(28.00, "El Principito", "Antoine de Saint-Exupéry", "Salamandra", 1943)

#obj libro 
libro1 = Libro("Ficción")
libro2 = Libro("Ciencia Ficción")
libro3 = Libro("Romance")
libro4 = Libro("Terror")

#obj revista 
revista1 = Revista("Tecnología")
revista2 = Revista("Deportes")
revista3 = Revista("Moda")
revista4 = Revista("Ciencia")

#obj Articulos segunda mano
articulo1 = ArticuloSegundaMano("Libro Usado", "Programación", "Juan Pérez")
articulo2 = ArticuloSegundaMano("Revista Usada", "Historia", "María López")
articulo3 = ArticuloSegundaMano("Libro Seminuevo", "Matemáticas", "Carlos Ruiz")

#obj novedades
novedad1 = Novedades("Nuevo Lanzamiento", "Ciencia Ficción")
novedad2 = Novedades("Best Seller", "Thriller")
novedad3 = Novedades("Recomendado", "Autoayuda")

#obj Aonline
articulo_online1 = ArticuloOnline("Inteligencia Artificial")
articulo_online2 = ArticuloOnline("Desarrollo Web")
articulo_online3 = ArticuloOnline("Machine Learning")

#obj hilo
hilo = Hilo()

#obj editorial
editorial1 = Editorial("Planeta", "Calle Principal 123", "555-1234")
editorial2 = Editorial("Salamandra", "Av. Libertad 456", "555-5678")
editorial3 = Editorial("Sudamericana", "Paseo Central 789", "555-9012")

#recolector obj
recolector = Recolector()
#servidor obj
servidor = Servidor()
#obj indexador
indexador = Indexador()
#obj procesador
procesador = Procesador()