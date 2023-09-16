from camelcase import camel_case
from unittest import TestCase

class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):
        
        self.assertEqual('helloWorld', camel_case('Hello World'))
        self.assertEqual('', camel_case('   '))
        self.assertEqual('😻😍💝💝', camel_case('😻 😍 💝💝'))
        self.assertEqual('helloWorld', camel_case('  Hello WOrLD  '))