class Usuario:
    # Metodo Constructor con parámetros
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


# Paso 3 obj
usuario1 = Usuario("Juan", "Pérez", "12345", "Calle 123", "juan123", "pass123")
usuario2 = Usuario("María", "López", "67890", "Av. Principal", "maria456", "pass456")

# Paso 4 llamar Métodos 
print("=== PROBANDO CLASE USUARIO ===")
print(usuario1.enviar_sugerencia())
print(usuario1.listar())
print(usuario1.comprar())
print(usuario1.vender())
print(usuario1.realizar_reclamacion())
print("\n--- Usuario 2 ---")
print(usuario2.listar())