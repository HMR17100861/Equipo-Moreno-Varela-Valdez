class Cliente:
    def __init__(self,id_cliente = None,razon_social = None, consignee = None) -> None:
        self.id_cliente = id_cliente
        self.razon_social = razon_social
        self.consignee = consignee
        

    def __str__(self) -> str:
        return f'Id del cliente:{self.id_cliente}, Razon Social: {self.razon_social}, Consignee:{self.consignee}'
