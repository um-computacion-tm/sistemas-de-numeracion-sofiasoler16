import unittest 

from cambiarbase import decimalbinario
from cambiarbase import binariodecimal

class test_numeracion(unittest.TestCase):
    def test_binariodecimal96(self):
        self.assertEqual (binariodecimal("01011100"), 92)
    def test_binariodecimal125(self):
        self.assertEqual (binariodecimal("01111101"), 125)
    def test_binariodecimal12(self):
        self.assertEqual (binariodecimal("1100"), 12)
    def test_binariodecimal89(self):
        self.assertEqual (binariodecimal("1011001"), 89)
    def test_binariodecimal7(self):
        self.assertEqual (binariodecimal("0111"), 7)


    def test_decimalbinario2(self):
       result =  decimalbinario(2)
       self.assertEqual(result, "10")
    def test_decimalbinario340(self):
       result =  decimalbinario(340)
       self.assertEqual(result, "0101010100")  
    def test_decimalbinario5(self):
       result =  decimalbinario(5)
       self.assertEqual(result, "0101") 
    def test_decimalbinario22(self):
       result =  decimalbinario(22)
       self.assertEqual(result, "010110")
    def test_decimalbinario7(self):
       result =  decimalbinario(7)
       self.assertEqual(result, "0111")
    def test_decimalbinario11(self):
       result =  decimalbinario(11)
       self.assertEqual(result, "01011")

if __name__ == "__main__":
    unittest.main()
