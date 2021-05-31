from django.test import TestCase
from .utils import DataBase

class DataBaseTest(TestCase):
    def setUp(self) -> None:
        self.database = DataBase()
        self.data = {
            'title': 'note',
            'text': 'note_text',
            'create': '2021-05-05',
            'id': 1
        }

    def test(self):
        self.assertEqual(self.database.create(self.data), True)
        self.assertEqual(len(self.database.all()), 1)
        self.assertEqual(self.database.update(self.data), True)
        self.assertEqual(self.database.delete(1), True)
