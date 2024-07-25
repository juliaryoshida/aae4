import unittest
from datetime import datetime
from agenda import Evento, Agenda

class TestAgenda(unittest.TestCase):

    def setUp(self):
        self.agenda = Agenda()

    def criar_evento(self, nome, inicio, fim):
        return Evento(nome, inicio, fim)

    def test_adicionar_evento_sem_conflito(self):
        evento = self.criar_evento("Reunião", "2024-07-25 10:00", "2024-07-25 11:00")
        resultado = self.agenda.adicionar_evento(evento)
        self.assertTrue(resultado, "O evento deveria ser adicionado com sucesso.")
        self.assertEqual(len(self.agenda.eventos), 1, "Deveria haver um evento na agenda.")

    def test_adicionar_evento_com_conflito(self):
        evento1 = self.criar_evento("Reunião", "2024-07-25 10:00", "2024-07-25 11:00")
        evento2 = self.criar_evento("Almoço", "2024-07-25 10:30", "2024-07-25 11:30")
        self.agenda.adicionar_evento(evento1)
        resultado = self.agenda.adicionar_evento(evento2)
        self.assertFalse(resultado, "O evento não deveria ser adicionado devido a conflito.")
        self.assertEqual(len(self.agenda.eventos), 1, "Deveria haver apenas um evento na agenda.")

    def test_adicionar_evento_apos_fim_do_outro(self):
        evento1 = self.criar_evento("Reunião", "2024-07-25 10:00", "2024-07-25 11:00")
        evento2 = self.criar_evento("Almoço", "2024-07-25 11:00", "2024-07-25 12:00")
        self.agenda.adicionar_evento(evento1)
        resultado = self.agenda.adicionar_evento(evento2)
        self.assertTrue(resultado, "O evento deveria ser adicionado com sucesso, pois não há conflito.")
        self.assertEqual(len(self.agenda.eventos), 2, "Deveria haver dois eventos na agenda.")

    def test_adicionar_evento_antes_inicio_do_outro(self):
        evento1 = self.criar_evento("Reunião", "2024-07-25 10:00", "2024-07-25 11:00")
        evento2 = self.criar_evento("Almoço", "2024-07-25 09:00", "2024-07-25 10:00")
        self.agenda.adicionar_evento(evento1)
        resultado = self.agenda.adicionar_evento(evento2)
        self.assertTrue(resultado, "O evento deveria ser adicionado com sucesso, pois não há conflito.")
        self.assertEqual(len(self.agenda.eventos), 2, "Deveria haver dois eventos na agenda.")

if __name__ == '__main__':
    unittest.main()
