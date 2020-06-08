

class Evento:
    def __init__(self, titulo, data_evento, descricao, usuario):
        self.__titulo = titulo
        self.__data_evento = data_evento
        self.__descricao = descricao
        self.__usuario = usuario

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def data_evento(self):
        return self.__data_evento

    @data_evento.setter
    def titulo(self, data_evento):
        self.__data_evento = data_evento

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario