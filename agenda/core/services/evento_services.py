from ..models import Evento
from datetime import datetime

def get_eventos(user):
    data_atual = datetime.now()
    return Evento.objects.filter(usuario=user,
                                 data_evento__gt=data_atual)

def get_last_eventos(user):
    data_atual = datetime.now()
    return Evento.objects.filter(usuario=user,
                                 data_evento__lt=data_atual)

def cadastrar_evento(titulo, data_evento, descricao, usuario):
    Evento.objects.create(titulo=titulo,
                          data_evento=data_evento,
                          descricao=descricao,
                          usuario=usuario)
def get_evento_by_id(id):
    return Evento.objects.get(id=id)

def update_evento(id, titulo, data_evento, descricao, usuario):
    Evento.objects.filter(id=id).update(
                          titulo=titulo,
                          data_evento=data_evento,
                          descricao=descricao,
                          usuario=usuario)

def delete_evento(id):
    Evento.objects.get(id=id).delete()

