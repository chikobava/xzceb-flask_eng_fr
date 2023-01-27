'''
translator module tests
'''
import unittest
import translator

class TestFrenchToEnglish(unittest.TestCase):
    '''
    tests for translation fr -> en
    '''

    def test_bonjour(self):
        '''
        test 'hello' translation into french
        '''
        self.assertEqual('Hello', translator.french_to_english('Bonjour'))

    def test_empty(self):
        '''
        test empty string
        '''
        self.assertEqual('', translator.french_to_english(''))


class TestEnglishToFrench(unittest.TestCase):
    '''
    tests for translation en -> fr
    '''

    def test_hello(self):
        '''
        test 'bounjour' translation into english
        '''
        self.assertEqual('Bonjour', translator.english_to_french('Hello'))

    def test_empty(self):
        '''
        test empty string
        '''
        self.assertEqual('', translator.english_to_french(''))


if __name__ == '__main__':
    unittest.main(verbosity=2)
