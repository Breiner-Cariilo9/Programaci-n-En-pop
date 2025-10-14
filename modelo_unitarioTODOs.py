# ==================== CLASE USUARIO ====================
class Usuario:
    # Constructor
    def __init__(self, nombre, apellido, nr_cuenta, direccion, login, password):
        # Atributos
        self.nombre = nombre
        self.apellido = apellido
        self.nr_cuenta = nr_cuenta
        self.direccion = direccion
        self.login = login
        self.password = password
    
    # Métodos Get
    def get_nombre(self):
        return self.nombre
    
    def get_apellido(self):
        return self.apellido
    
    def get_nr_cuenta(self):
        return self.nr_cuenta
    
    def get_direccion(self):
        return self.direccion
    
    def get_login(self):
        return self.login
    
    # Métodos Set
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_apellido(self, apellido):
        self.apellido = apellido
    
    def set_nr_cuenta(self, nr_cuenta):
        self.nr_cuenta = nr_cuenta
    
    def set_direccion(self, direccion):
        self.direccion = direccion
    
    def set_login(self, login):
        self.login = login
    
    def set_password(self, password):
        self.password = password
    
    # Métodos normales
    def enviar_sugerencia(self, sugerencia):
        return f"Sugerencia enviada: {sugerencia}"
    
    def leer(self):
        return "Usuario está leyendo"
    
    def comprar(self, producto):
        return f"Comprando: {producto}"
    
    def vender(self, producto):
        return f"Vendiendo: {producto}"
    
    def realizar_reclamacion(self, reclamacion):
        return f"Reclamación realizada: {reclamacion}"


# ==================== CLASE PRODUCTO ====================
class Producto:
    # Constructor
    def __init__(self, precio, titulo, autor, editorial, anio_edicion, preferencias):
        # Atributos
        self.precio = precio
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.anio_edicion = anio_edicion
        self.preferencias = preferencias
    
    # Métodos Get
    def get_precio(self):
        return self.precio
    
    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor
    
    def get_editorial(self):
        return self.editorial
    
    def get_anio_edicion(self):
        return self.anio_edicion
    
    def get_preferencias(self):
        return self.preferencias
    
    # Métodos Set
    def set_precio(self, precio):
        self.precio = precio
    
    def set_titulo(self, titulo):
        self.titulo = titulo
    
    def set_autor(self, autor):
        self.autor = autor
    
    def set_editorial(self, editorial):
        self.editorial = editorial
    
    def set_anio_edicion(self, anio_edicion):
        self.anio_edicion = anio_edicion
    
    def set_preferencias(self, preferencias):
        self.preferencias = preferencias
    
    # Métodos normales
    def vender(self):
        return f"Vendiendo producto: {self.titulo}"
    
    def comprar(self):
        return f"Comprando producto: {self.titulo}"
    
    def ver_catalogo(self):
        return f"Catálogo - Título: {self.titulo}, Autor: {self.autor}, Precio: ${self.precio}"


# ==================== CLASE LIBRO ====================
class Libro(Producto):
    # Constructor
    def __init__(self, precio, titulo, autor, editorial, anio_edicion, preferencias, genero):
        # Llamar al constructor de la clase padre
        super().__init__(precio, titulo, autor, editorial, anio_edicion, preferencias)
        # Atributo específico
        self.genero = genero
    
    # Métodos Get
    def get_genero(self):
        return self.genero
    
    # Métodos Set
    def set_genero(self, genero):
        self.genero = genero


# ==================== CLASE REVISTA ====================
class Revista(Producto):
    # Constructor
    def __init__(self, precio, titulo, autor, editorial, anio_edicion, preferencias, categoria):
        # Llamar al constructor de la clase padre
        super().__init__(precio, titulo, autor, editorial, anio_edicion, preferencias)
        # Atributo específico
        self.categoria = categoria
    
    # Métodos Get
    def get_categoria(self):
        return self.categoria
    
    # Métodos Set
    def set_categoria(self, categoria):
        self.categoria = categoria


# ==================== CLASE ARTICULO DE SEGUNDA MANO ====================
class ArticuloSegundaMano(Producto):
    # Constructor
    def __init__(self, precio, titulo, autor, editorial, anio_edicion, preferencias, clasificacion, tema, vendedor):
        # Llamar al constructor de la clase padre
        super().__init__(precio, titulo, autor, editorial, anio_edicion, preferencias)
        # Atributos específicos
        self.clasificacion = clasificacion
        self.tema = tema
        self.vendedor = vendedor
    
    # Métodos Get
    def get_clasificacion(self):
        return self.clasificacion
    
    def get_tema(self):
        return self.tema
    
    def get_vendedor(self):
        return self.vendedor
    
    # Métodos Set
    def set_clasificacion(self, clasificacion):
        self.clasificacion = clasificacion
    
    def set_tema(self, tema):
        self.tema = tema
    
    def set_vendedor(self, vendedor):
        self.vendedor = vendedor


# ==================== CLASE NOVEDADES ====================
class Novedades:
    # Constructor
    def __init__(self, clasificacion, tema):
        # Atributos
        self.clasificacion = clasificacion
        self.tema = tema
    
    # Métodos Get
    def get_clasificacion(self):
        return self.clasificacion
    
    def get_tema(self):
        return self.tema
    
    # Métodos Set
    def set_clasificacion(self, clasificacion):
        self.clasificacion = clasificacion
    
    def set_tema(self, tema):
        self.tema = tema
    
    # Método normal
    def cambiar_clasificacion(self, nueva_clasificacion):
        self.clasificacion = nueva_clasificacion
        return f"Clasificación cambiada a: {nueva_clasificacion}"


# ==================== CLASE ARTICULO ONLINE ====================
class ArticuloOnline:
    # Constructor
    def __init__(self, tema):
        # Atributo
        self.tema = tema
    
    # Métodos Get
    def get_tema(self):
        return self.tema
    
    # Métodos Set
    def set_tema(self, tema):
        self.tema = tema
    
    # Método normal
    def publicar(self):
        return f"Artículo online publicado sobre: {self.tema}"


# ==================== CLASE HILO ====================
class Hilo:
    # Constructor
    def __init__(self):
        # Atributo
        self.novedades = []
    
    # Método normal
    def buscar_novedades(self):
        return f"Buscando novedades... {len(self.novedades)} encontradas"


# ==================== CLASE EDITORIAL ====================
class Editorial:
    # Constructor
    def __init__(self, nombre, direccion, telefono):
        # Atributos
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
    
    # Métodos Get
    def get_nombre(self):
        return self.nombre
    
    def get_direccion(self):
        return self.direccion
    
    def get_telefono(self):
        return self.telefono
    
    # Métodos Set
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_direccion(self, direccion):
        self.direccion = direccion
    
    def set_telefono(self, telefono):
        self.telefono = telefono
    
    # Método normal
    def vender(self, producto):
        return f"Editorial {self.nombre} vendiendo: {producto}"


# ==================== CLASE RECOLECTOR ====================
class Recolector:
    # Constructor
    def __init__(self):
        # Atributo
        self.novedades = []
    
    # Método normal
    def envia_novedades(self, novedad):
        self.novedades.append(novedad)
        return f"Novedad agregada. Total: {len(self.novedades)}"


# ==================== CLASE SERVIDOR ====================
class Servidor:
    # Constructor
    def __init__(self):
        # Atributos
        self.paginas = []
        self.sugerencias = []
        self.datos_compra = []
        self.datos_venta = []
    
    # Métodos normales
    def muestra_pagina(self, pagina):
        return f"Mostrando página: {pagina}"
    
    def envia_sugerencia(self, sugerencia):
        self.sugerencias.append(sugerencia)
        return f"Sugerencia recibida: {sugerencia}"
    
    def envia_datos_de_compra(self, datos):
        self.datos_compra.append(datos)
        return f"Datos de compra registrados"
    
    def envia_datos_de_venta(self, datos):
        self.datos_venta.append(datos)
        return f"Datos de venta registrados"


# ==================== CLASE INDEXADOR ====================
class Indexador:
    # Constructor
    def __init__(self):
        # Atributo
        self.almacen = []
    
    # Métodos normales
    def actualiza_almacen(self, producto):
        self.almacen.append(producto)
        return f"Almacén actualizado. Total productos: {len(self.almacen)}"
    
    def envia_resultado_busqueda(self, criterio):
        return f"Resultados de búsqueda para: {criterio}"


# ==================== CLASE PROCESADOR ====================
class Procesador:
    # Constructor
    def __init__(self):
        # Atributos internos
        self.datos_venta = []
        self.archivos_online = []
        self.administrador = None
    
    # Métodos normales
    def mandar_datos_de_venta(self, datos):
        self.datos_venta.append(datos)
        return "Datos de venta procesados"
    
    def mandar_archivo_online(self, archivo):
        self.archivos_online.append(archivo)
        return "Archivo online enviado"
    
    def mandar_info_administrador(self, info):
        self.administrador = info
        return "Información enviada al administrador"
    
    def modificar_stock(self, producto, cantidad):
        return f"Stock modificado: {producto} - Cantidad: {cantidad}"
    
    def realizar_cobro(self, monto):
        return f"Cobro realizado: ${monto}"
    
    def realizar_pago(self, monto):
        return f"Pago realizado: ${monto}"
    
    def realiza_catalogo(self):
        return "Catálogo generado"
    
    def realiza_busqueda(self, criterio):
        return f"Búsqueda realizada: {criterio}"


# ==================== EJEMPLO DE USO (INSTANCIAS) ====================
if __name__ == "__main__":
    # Crear instancia de Usuario
    usuario1 = Usuario("Juan", "Pérez", "123456", "Calle 123", "juanp", "pass123")
    print(f"Usuario creado: {usuario1.get_nombre()} {usuario1.get_apellido()}")
    
    # Crear instancia de Libro
    libro1 = Libro(25000, "Cien Años de Soledad", "Gabriel García Márquez", 
                   "Editorial Sudamericana", 1967, "Bestseller", "Ficción")
    print(f"\nLibro creado: {libro1.ver_catalogo()}")
    print(f"Género: {libro1.get_genero()}")
    
    # Crear instancia de Revista
    revista1 = Revista(5000, "National Geographic", "Varios", "NatGeo", 2025, 
                       "Popular", "Ciencia")
    print(f"\nRevista: {revista1.get_titulo()} - Categoría: {revista1.get_categoria()}")
    
    # Crear instancia de Editorial
    editorial1 = Editorial("Norma", "Bogotá, Colombia", "3001234567")
    print(f"\nEditorial: {editorial1.get_nombre()}")
    
    print("\n¡Todas las clases creadas exitosamente!")