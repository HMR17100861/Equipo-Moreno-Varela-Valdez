class Proveedor:
    def __init__(self,id_proveedor = None,razon_social = None, shipper = None) -> None:
        self.id_proveedor = id_proveedor
        self.razon_social = razon_social
        self.shipper = shipper
        

    def __str__(self) -> str:
        return f'Id del Proveedor: {self.id_proveedor}, Razon Social:{self.razon_social}, Shipper: {self.shipper}'
