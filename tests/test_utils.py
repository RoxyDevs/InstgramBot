import unittest
from utils.instagram_utils import some_function_to_test

class TestInstagramUtils(unittest.TestCase):

    def test_some_function_to_test(self):
        # Configurar los datos de prueba
        input_data = 'test_input'
        expected_output = 'expected_output'
        
        # Llamar a la función y verificar el resultado
        result = some_function_to_test(input_data)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()