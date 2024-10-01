from config.db import connectToMySQL
from productos import Productos

class Carrito_Builer:
    def __init__(self, data):
        self.idcarrito = data["idcarrito"]
        self.cantidad = data["cantidad"]
        self.usuarios_idusuarios = data["usuarios_idusuarios"]
        self.productos_idproductos = data["productos_idproductos"]
        self.guardar_producto = None
        
    classmethod
    def get_element(cls, usuarios_idusuarios, productos_idproductos):
        query = f"SELECT * FROM carrito WHERE usuarios_idusuarios={usuarios_idusuarios} AND productos_idproductos={productos_idproductos}"
        result = connectToMySQL("ejemplo_carrito").query_db(query)
        productos = []
        for producto in result:
            productos.append(cls(producto))
        return productos
    
    @classmethod
    def insert(cls, usuarios_idusuarios, productos_idproductos):
        query = f"INSERT INTO carrito (usuarios_idusuarios, productos_idproductos, cantidad) VALUES ({usuarios_idusuarios},{productos_idproductos}, 1)"
        result = connectToMySQL("ejemplo_carrito").query_db(query)
        return result
    
    @classmethod
    def select_all(cls, usuarios_idusuarios):
        query = f"""
            SELECT * FROM carrito 
            LEFT JOIN guardar_producto 
            ON carrito.productos_idproductos=productos_idproductos 
            WHERE usuarios_idusuarios={usuarios_idusuarios}"""
        result = connectToMySQL("ejemplo_carrito").query_db(query)
        productos = []
        for producto in result:
            tmp = cls(producto)
            tmp.guardar_producto = Productos(producto)
            productos.append(tmp)
        return productos
    
    @classmethod
    def update_cant(cls, cantidad, idcarrito):
        query = f"UPDATE carrito SET cantidad={cantidad} WHERE idcarrito={idcarrito}"
        result = connectToMySQL("ejemplo_carrito").query_db(query)
        return result
    
    @classmethod
    def delete_cart(cls, usuarios_idusuarios):
        query = f"DELETE FROM carrito WHERE usuarios_idusuarios={usuarios_idusuarios}"
        result = connectToMySQL("ejemplo_carrito").query_db(query)
        return result