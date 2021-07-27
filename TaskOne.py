import unittest
# импортируем модуль с функциями по бухгалтерии
from Testing.bookkeeping import check_document_existance, delete_doc, add_new_doc


class TestFunctions(unittest.TestCase):
    def setUp(self):
        print('method setUp')

    def tearDown(self):
        print('method tearDown')

    def test_document_existance(self):
        self.assertTrue(check_document_existance('2207 876234'))
        self.assertFalse(check_document_existance('231'))

    def test_add_new_doc(self):
        self.assertEqual(add_new_doc('007', 'passport', 'Jack', 5), 5)

    def test_delete_a_doc(self):
        self.assertEqual(delete_doc('10006'), ('10006', True))


if __name__ == '__main__':
    unittest.main()
