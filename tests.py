'''Tests for translation modules'''

import unittest

from translator import englishtofrench, englishtogerman

class TestEnglishtofrench(unittest.TestCase):
    '''Tests English to French function'''
    def test1(self):
        '''Tests null, hello and snake translations'''
        self.assertEqual(englishtofrench(None), '')
        self.assertEqual(englishtofrench('Hello'), 'Bonjour')
        self.assertEqual(englishtofrench('snake'), 'serpent')

class TestEnglishtogerman(unittest.TestCase):
    '''Tests English to German function'''
    def test1(self):
        '''Tests null, hello and snake translations'''
        self.assertEqual(englishtogerman(None), '')
        self.assertEqual(englishtogerman('Hello'), 'Hallo')
        self.assertEqual(englishtogerman('snake'), 'schlange')

unittest.main()
