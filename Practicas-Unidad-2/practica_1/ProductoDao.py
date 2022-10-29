from Producto import Producto 
from Conexion import Conexion
from logger_base import log
from cursor_del_pool import CursorDelPool

class ProductoDao:
    _SELECCIONAR = "SELECT * FROM producto"
    _INSERTAR = "INSERT INTO producto(nombre, descripcion) VALUES (%s,%s)"
    _ACTUALIZAR = "UPDATE producto SET nombre = %s, descripcion = %s WHERE id_producto = %s"
    _ELIMINAR = "DELETE FROM producto WHERE id_producto = %s"

    @classmethod
    def seleccionar(cls):
       with CursorDelPool() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                productos = []
                for r in registros:
                    producto = Producto(r[0],r[1],r[2])
                    productos.append(producto)
                return productos

    @classmethod
    def insertar(cls, producto):
        with CursorDelPool() as cursor:
            valores = (producto.nombre, producto.descripcion)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount
    
    @classmethod
    def actualizar(cls,producto):
        with CursorDelPool() as cursor:
            valores = (producto.nombre, producto.descripcion, producto.id_producto)
            cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls,producto):
        with CursorDelPool() as cursor:
            cursor.execute(cls._ELIMINAR, producto.id_producto)
            return cursor.rowcount

if __name__ == '__main__':
    #Insertar 
    
    Producto1 = Producto(nombre="Monitor",descripcion="Marca Samsung, color negro, 24 pulgadas, 1920x1080, 60Hz")
    personasInsertadas =+ ProductoDao.insertar(Producto1)
    log.debug(f'Personas insertadas {personasInsertadas}')

    Producto1 = Producto(nombre="Laptop",descripcion="Marca Lenovo, color azul, 15 pulgadas, 1920x1080, 60Hz")
    personasInsertadas =+ProductoDao.insertar(Producto1)
    log.debug(f'Personas insertadas {personasInsertadas}')
    
    Producto1 = Producto(nombre="Escritorio",descripcion="Hecho de madera, con rgb y 4 puertos usb")
    personasInsertadas =+ ProductoDao.insertar(Producto1)
    log.debug(f'Personas insertadas {personasInsertadas}')
    #Actualizar
    Producto1 = Producto(nombre="Escritorio",descripcion="Hecho de madera y rgb", id_producto=3)
    personasActualizadas = ProductoDao.actualizar(Producto1)
    log.debug(f'Personas actualizadas {personasActualizadas}')

    #Eliminar
    Producto1 = Producto(id_producto = '2')
    personasEliminadas = ProductoDao.eliminar(Producto1)
    log.debug(f'Personas eliminadas {personasEliminadas}')
    #ver
    productos = ProductoDao.seleccionar()
    for p in productos:
        log.debug(p)