import unittest
from .hex_to_string import hex_to_string

class MyTestCase(unittest.TestCase):
    def test_hex_to_string(self):
        hexs = [[0x10, 0x20, 0x30], [0x40, 0x50, 0x60]]
        value = '{{0x10,0x20,0x30},{0x40,0x50,0x60}}'
        result = hex_to_string(hexs)
        self.assertEqual(result, value)



if __name__ == '__main__':
    unittest.main()
