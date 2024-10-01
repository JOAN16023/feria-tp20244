from config.db import connectToMySQL

class Productos:
    def __init__(self, data):
        self.id = data["idproductos"]
        self.nombre = data["nombre"]
        self.precio = data["precio"]


    @classmethod
    def select_all(cls):
        query = "SELECT * FROM productos"
        result = connectToMySQL("ejemplo_carrito").query_db(query)
        productos = []
        for producto in result:
            productos.append(cls(producto))
        return productos