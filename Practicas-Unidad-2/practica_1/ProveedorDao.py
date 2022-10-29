from Conexion import Conexion
from cursor_del_pool import CursorDelPool
from logger_base import log
from Proveedor import Proveedor


class ProveedorDao:
    _SELECCIONAR = "SELECT * FROM proveedor"
    _INSERTAR = "INSERT INTO proveedor(razon_social, shipper) VALUES (%s,%s)"
    _ACTUALIZAR = "UPDATE proveedor SET razon_social = %s, shipper = %s WHERE id_proveedor = %s"
    _ELIMINAR = "DELETE FROM proveedor WHERE id_proveedor = %s"

    @classmethod
    def seleccionar(cls):
       with CursorDelPool() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                proveedores = []
                for r in registros:
                    proveedor = Proveedor(r[0],r[1],r[2])
                    proveedores.append(proveedor)
                return proveedores

    @classmethod
    def insertar(cls, proveedor):
        with CursorDelPool() as cursor:
            valores = (proveedor.razon_social, proveedor.shipper)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount
    
    @classmethod
    def actualizar(cls,proveedor):
        with CursorDelPool() as cursor:
            valores = (proveedor.razon_social, proveedor.shipper, proveedor.id_proveedor)
            cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls,proveedor):
        with CursorDelPool() as cursor:
            cursor.execute(cls._ELIMINAR, proveedor.id_proveedor)
            return cursor.rowcount

if __name__ == '__main__':
    #Insertar  
    Proveedor1 = Proveedor(razon_social="T1",shipper="G1234567")
    personasInsertadas = ProveedorDao.insertar(Proveedor1)
    log.debug(f'Proveedores insertadas {personasInsertadas}')

    Proveedor1 = Proveedor(razon_social="GENG",shipper="G2224267")
    personasInsertadas = ProveedorDao.insertar(Proveedor1)
    log.debug(f'Proveedores insertadas {personasInsertadas}')
    
    Proveedor1 = Proveedor(razon_social="DRX",shipper="G9999997")
    personasInsertadas = ProveedorDao.insertar(Proveedor1)
    log.debug(f'Proveedores insertadas {personasInsertadas}')

    # #Actualizar
    Proveedor1 = Proveedor(razon_social="JDG",shipper="G1777737", id_proveedor=3)
    personasActualizadas = ProveedorDao.actualizar(Proveedor1)
    log.debug(f'Proveedores actualizadas {personasActualizadas}')

    #Eliminar
    Proveedor1 = Proveedor(id_proveedor= '2')
    personasEliminadas = ProveedorDao.eliminar(Proveedor1)
    log.debug(f'Proveedores eliminadas {personasEliminadas}')
    #ver
    proveedores = ProveedorDao.seleccionar()
    for p in proveedores:
        log.debug(p)
