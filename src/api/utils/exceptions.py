class ObjectNotFoundException(Exception):
    """
    Representa um erro quando o objeto com determinado ID não é encontrado.
    """

    def __init__(self, obj_type: str, obj_id: str):
        super().__init__(f'{obj_type} with ID [{obj_id}] not found')
