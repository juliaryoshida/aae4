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

    def tem_conflito(self, novo_evento):
        return any(novo_evento.conflita_com(e) for e in self.eventos)

    def adicionar_evento(self, evento):
        if self.tem_conflito(evento):
            return False
        self.eventos.append(evento)
        return True

    def remover_evento(self, nome):
        eventos_filtrados = [evento for evento in self.eventos if evento.nome != nome]
        if len(eventos_filtrados) == len(self.eventos):
            return False  # Nenhum evento removido
        self.eventos = eventos_filtrados
        return True

    def mostrar_agenda(self):
        if not self.eventos:
            return "Nenhum evento agendado."
        return "\n".join(
            [f"{evento.nome}: {evento.inicio.strftime('%Y-%m-%d %H:%M')} a {evento.fim.strftime('%Y-%m-%d %H:%M')}"
             for evento in self.eventos]
        )

def main():
    agenda = Agenda()
    
    while True:
        print("\nAgenda de Eventos")
        print("1. Adicionar evento")
        print("2. Listar eventos")
        print("3. Sair")
        
        escolha = input("Escolha uma opção (1/2/3): ")
        
        if escolha == "1":
            nome = input("Digite o nome do evento: ")
            inicio = input("Digite a data e hora de início (YYYY-MM-DD HH:MM): ")
            fim = input("Digite a data e hora de término (YYYY-MM-DD HH:MM): ")
            
            try:
                evento = Evento(nome, inicio, fim)
                if agenda.adicionar_evento(evento):
                    print("Evento adicionado com sucesso.")
                else:
                    print("Conflito de agendamento detectado. Evento não adicionado.")
            except ValueError:
                print("Formato de data e hora inválido. Tente novamente.")

        elif escolha == "2":
            if agenda.eventos:
                print("\nEventos na agenda:")
                for e in agenda.eventos:
                    print(f"{e.nome}: {e.inicio} - {e.fim}")
            else:
                print("Nenhum evento na agenda.")

        elif escolha == "3":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
