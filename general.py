# ==================== CLASE USUARIO ====================
class Usuario:
    # coatructor con parametros
    def __init__(self, nombre, apellido, num_cuenta, direccion, login, password):
        self.nombre = nombre
        self.apellido = apellido
        self.num_cuenta = num_cuenta
        self.direccion = direccion
        self.login = login
        self.password = password
    
    # clases
    def enviar_sugerencia(self):
        print(f"Usuario {self.nombre} envía sugerencia")
        return "Sugerencia enviada"
    
    def listar(self):
        print(f"Listando datos del usuario {self.nombre}")
        return f"Usuario: {self.nombre} {self.apellido}, Cuenta: {self.num_cuenta}"
    
    def comprar(self):
        print(f"{self.nombre} está realizando una compra")
        return "Compra procesada"
    
    def vender(self):
        print(f"{self.nombre} está realizando una venta")
        return "Venta procesada"
    
    def realizar_reclamacion(self):
        print(f"{self.nombre} realiza una reclamación")
        return "Reclamación registrada"


# obj
usuario1 = Usuario("Juan", "Pérez", "12345", "Calle 123", "juan123", "pass123")
usuario2 = Usuario("María", "López", "67890", "Av. Principal", "maria456", "pass456")

# llamar Métodos 
print("=== PROBANDO CLASE USUARIO ===")
print(usuario1.enviar_sugerencia())
print(usuario1.listar())
print(usuario1.comprar())
print(usuario1.vender())
print(usuario1.realizar_reclamacion())
print("\n--- Usuario 2 ---")
print(usuario2.listar())


# ==================== CLASE PRODUCTO ====================

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

# llamar Métodos -> Argumento 
print("=== PROBANDO CLASE PRODUCTO ===")
print(producto1.ver_catalogo())
print(producto1.vender())
print(producto1.comprar())
print("\n--- Producto 2 ---")
print(producto2.ver_catalogo())
print("\n--- Producto 3 ---")
print(producto3.ver_catalogo())


# ==================== CLASE LIBRO ====================

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

# ==================== CLASE REVISTA ====================
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

# ==================== CLASE ARTICULO DE SEGUNDA MANO ====================

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

# ==================== CLASE NOVEDADES ====================

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

# ==================== CLASE ARTICULO ONLINE ====================

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

# ==================== CLASE HILO ====================

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

# ==================== CLASE EDITORIAL ====================

class Editorial:

    
    #metodo Constructor con parámetros
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
    
   
    def vender(self):
        print(f"Editorial {self.nombre} está vendiendo publicaciones")
        return f"Venta realizada por {self.nombre}"



editorial1 = Editorial("Planeta", "Calle Principal 123", "555-1234")
editorial2 = Editorial("Salamandra", "Av. Libertad 456", "555-5678")
editorial3 = Editorial("Sudamericana", "Paseo Central 789", "555-9012")

#llamar Métodos -> Argumento -> E.D
print("=== PROBANDO CLASE EDITORIAL ===")
print(f"Editorial: {editorial1.nombre}, Dirección: {editorial1.direccion}, Teléfono: {editorial1.telefono}")
print(editorial1.vender())
print(f"\nEditorial: {editorial2.nombre}, Dirección: {editorial2.direccion}, Teléfono: {editorial2.telefono}")
print(editorial2.vender())

# ==================== CLASE RECOLECTOR ====================

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


# ==================== CLASE SERVIDOR ====================

class Servidor:
    # No necesitamos constructor con parámetros según el diagrama no ahi atributos
    
    # Paso 2: funciones
    def nuestra_pagina_metodo(self):
        print("Ejecutando nuestra_pagina()")
        return "Página principal cargada"
    
    def envia_sugerencia_metodo(self):
        print("Ejecutando envia_sugerencia()")
        return "Sugerencia enviada al usuario"
    
    def envia_datos_de_comprar_metodo(self):
        print("Ejecutando envia_datos_de_comprar()")
        return "Datos de compra enviados"
    
    def envia_datos_de_venta_metodo(self):
        print("Ejecutando envia_datos_de_venta()")
        return "Datos de venta enviados"

#codigo principal
# Paso 3: hacer obj -> Argumentos
servidor = Servidor()

# Paso 4: llamar Métodos
print("=== PROBANDO CLASE SERVIDOR ===")
print(servidor.nuestra_pagina_metodo())
print(servidor.envia_sugerencia_metodo())
print(servidor.envia_datos_de_comprar_metodo())
print(servidor.envia_datos_de_venta_metodo())

# ==================== CLASE INDEXADOR ====================

class Indexador:
  # clases
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

# ==================== CLASE PROCESADOR ====================

class Procesador:
# metodos Normales
    def mandar_datos_de_venta_metodo(self, datos_venta):
        print(f"Mandando datos de venta: {datos_venta}")
        return "Datos de venta enviados"
    
    def mandar_archivo_online_metodo(self, archivo):
        print(f"Mandando archivo online: {archivo}")
        return "Archivo subido correctamente"
    
    def validar_datos_administrador_metodo(self, usuario, password):
        print(f"Validando administrador: {usuario}")
        if usuario == "admin" and password == "admin123":
            return "Administrador validado"
        return "Credenciales incorrectas"
    
    def modificar_stock_metodo(self, producto, cantidad):
        print(f"Modificando stock de {producto}: {cantidad} unidades")
        return f"Stock actualizado: {producto} = {cantidad}"
    
    def realizar_cobro_metodo(self, monto):
        print(f"Realizando cobro de ${monto}")
        return f"Cobro procesado: ${monto}"
    
    def realizar_pago_metodo(self, monto):
        print(f"Realizando pago de ${monto}")
        return f"Pago procesado: ${monto}"
    
    def actualiza_catalogo_metodo(self):
        print("Actualizando catálogo de productos...")
        return "Catálogo actualizado"
    
    def realiza_busqueda_metodo(self, termino):
        print(f"Realizando búsqueda de: {termino}")
        return f"Resultados para: {termino}"


#hacer obj
procesador = Procesador()

#llamar Métodos
print("=== PROBANDO CLASE PROCESADOR ===")
print(procesador.mandar_datos_de_venta_metodo("Venta #001"))
print(procesador.mandar_archivo_online_metodo("documento.pdf"))
print(procesador.validar_datos_administrador_metodo("admin", "admin123"))
print(procesador.modificar_stock_metodo("Laptop", 50))
print(procesador.realizar_cobro_metodo(150.00))
print(procesador.realizar_pago_metodo(75.50))
print(procesador.actualiza_catalogo_metodo())
print(procesador.realiza_busqueda_metodo("mouse inalámbrico"))