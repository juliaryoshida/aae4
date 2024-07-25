from datetime import datetime

class Evento:
    def __init__(self, nome, inicio, fim):
        self.nome = nome
        self.inicio = datetime.strptime(inicio, "%Y-%m-%d %H:%M")
        self.fim = datetime.strptime(fim, "%Y-%m-%d %H:%M")

    def conflita_com(self, outro_evento):
        return self.inicio < outro_evento.fim and self.fim > outro_evento.inicio

class Agenda:
    def __init__(self):
        self.eventos = []

    def adicionar_evento(self, evento):
        if any(evento.conflita_com(e) for e in self.eventos):
            return False
        self.eventos.append(evento)
        return True
