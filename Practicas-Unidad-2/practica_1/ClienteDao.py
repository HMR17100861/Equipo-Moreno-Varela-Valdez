from Cliente import Cliente 
from Conexion import Conexion
from logger_base import log
from cursor_del_pool import CursorDelPool

class ClienteDao:
    _SELECCIONAR = "SELECT * FROM cliente"
    _INSERTAR = "INSERT INTO cliente(razon_social, consignee) VALUES (%s,%s)"
    _ACTUALIZAR = "UPDATE cliente SET razon_social = %s, consignee = %s WHERE id_cliente = %s"
    _ELIMINAR = "DELETE FROM cliente WHERE id_cliente = %s"

    @classmethod
    def seleccionar(cls):
       with CursorDelPool() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                clientes = []
                for r in registros:
                    cliente = Cliente(r[0],r[1],r[2])
                    clientes.append(cliente)
                return clientes

    @classmethod
    def insertar(cls, cliente):
        with CursorDelPool() as cursor:
            valores = (cliente.razon_social, cliente.consignee)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount
    
    @classmethod
    def actualizar(cls,cliente):
        with CursorDelPool() as cursor:
            valores = (cliente.razon_social, cliente.consignee, cliente.id_cliente)
            cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls,cliente):
        with CursorDelPool() as cursor:
            cursor.execute(cls._ELIMINAR, cliente.id_cliente)
            return cursor.rowcount

if __name__ == '__main__':
    #Insertar 
    
    Cliente1 = Cliente(razon_social="KOTTY INC",consignee="G1234567")
    personasInsertadas = ClienteDao.insertar(Cliente1)
    log.debug(f'Clientes insertados {personasInsertadas}')

    Cliente1 = Cliente(razon_social="KOI",consignee="G2224267")
    personasInsertadas = ClienteDao.insertar(Cliente1)
    log.debug(f'Clientes insertados {personasInsertadas}')
    
    Cliente1 = Cliente(razon_social="MAXIMUS",consignee="G9999997")
    personasInsertadas = ClienteDao.insertar(Cliente1)
    log.debug(f'Clientes insertados {personasInsertadas}')
    #Actualizar
    Cliente1 = Cliente(razon_social="ROGUE",consignee="G1777737", id_cliente=2)
    personasActualizadas = ClienteDao.actualizar(Cliente1)
    log.debug(f'Clientes actualizados {personasActualizadas}')

    #Eliminar
    Cliente1 = Cliente(id_cliente = '3')
    personasEliminadas = ClienteDao.eliminar(Cliente1)
    log.debug(f'Clientes eliminados {personasEliminadas}')
    #ver
    clientes = ClienteDao.seleccionar()
    for c in clientes:
        log.debug(c)