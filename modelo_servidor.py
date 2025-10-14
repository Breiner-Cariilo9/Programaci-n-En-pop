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