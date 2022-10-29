class Producto:
    def __init__(self,id_producto = None,nombre = None, descripcion = None) -> None:
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        

    def __str__(self) -> str:
        return f'Id del Producto: {self.id_producto}, Nombre: {self.nombre}, Descripcion: {self.descripcion}'
