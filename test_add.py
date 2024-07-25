import unittest
from agenda import Evento, Agenda

class TestAgenda(unittest.TestCase):

    def setUp(self):
        self.agenda = Agenda()

    def test_adicionar_evento_sem_conflito(self):
        evento = Evento("Reunião", "2024-07-25 10:00", "2024-07-25 11:00")
        resultado = self.agenda.adicionar_evento(evento)
        self.assertTrue(resultado)
        self.assertEqual(len(self.agenda.eventos), 1) 
    
    def test_adicionar_evento_com_conflito(self):
        evento1 = Evento("Reunião", "2024-07-25 10:00", "2024-07-25 11:00")
        evento2 = Evento("Almoço", "2024-07-25 10:30", "2024-07-25 11:30")
        self.agenda.adicionar_evento(evento1)
        resultado = self.agenda.adicionar_evento(evento2)
        self.assertFalse(resultado)
        self.assertEqual(len(self.agenda.eventos), 1)

    def test_adicionar_evento_apos_fim_do_outro(self):
        evento1 = Evento("Reunião", "2024-07-25 10:00", "2024-07-25 11:00")
        evento2 = Evento("Almoço", "2024-07-25 11:00", "2024-07-25 12:00")
        self.agenda.adicionar_evento(evento1)
        resultado = self.agenda.adicionar_evento(evento2)
        self.assertTrue(resultado)
        self.assertEqual(len(self.agenda.eventos), 2)

    def test_adicionar_evento_antes_inicio_do_outro(self):
        evento1 = Evento("Reunião", "2024-07-25 10:00", "2024-07-25 11:00")
        evento2 = Evento("Almoço", "2024-07-25 09:00", "2024-07-25 10:00")
        self.agenda.adicionar_evento(evento1)
        resultado = self.agenda.adicionar_evento(evento2)
        self.assertTrue(resultado)
        self.assertEqual(len(self.agenda.eventos), 2)

if __name__ == '__main__':
    unittest.main()
