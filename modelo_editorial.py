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