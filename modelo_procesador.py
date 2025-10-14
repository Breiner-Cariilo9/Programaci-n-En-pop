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