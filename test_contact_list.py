import unittest
from app import app

class TestContactList(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_contact(self):
        # Dodawanie kontaktu
        response = self.app.post('/add_contact', data=dict(name="Jan Kowalski", phone="123456789"))
        self.assertEqual(response.status_code, 302)  # Sprawdzamy czy przekierowuje po dodaniu kontaktu
        # Sprawdzamy czy kontakt został dodany do listy
        response = self.app.get('/')
        self.assertIn(b'Jan Kowalski', response.data)  # Sprawdzamy czy imię nowego kontaktu jest widoczne na stronie

    def test_edit_contact(self):
        # Edycja kontaktu
        response = self.app.post('/edit_contact/John%20Doe', data=dict(name="John Smith", phone="987654321"))
        self.assertEqual(response.status_code, 302)  # Sprawdzamy czy przekierowuje po edycji kontaktu
        # Sprawdzamy czy kontakt został zmieniony w liście
        response = self.app.get('/')
        self.assertIn(b'John Smith', response.data)  # Sprawdzamy czy zmienione imię kontaktu jest widoczne na stronie

    def test_remove_contact(self):
        # Usunięcie kontaktu
        response = self.app.get('/delete_contact/Jane%20Smith')
        self.assertEqual(response.status_code, 302)  # Sprawdzamy czy przekierowuje po usunięciu kontaktu
        # Sprawdzamy czy kontakt został usunięty z listy
        response = self.app.get('/')
        self.assertNotIn(b'Jane Smith', response.data)  # Sprawdzamy czy imię usuniętego kontaktu nie jest widoczne na stronie

if __name__ == '__main__':
    unittest.main()
