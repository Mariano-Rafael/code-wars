class RequestType:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# Lista de tipos de solicitação
request_types = [
    RequestType(1, 'Reclamação'),
    RequestType(2, 'Sugestão'),
    RequestType(3, 'Dúvida'),
    RequestType(4, 'Informações'),
]