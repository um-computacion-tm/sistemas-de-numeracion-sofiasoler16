import unittest 

from cambiarbase import decimalbinario
from cambiarbase import binariodecimal
from cambiarbase import decitohexa
from cambiarbase import decitoocta
from cambiarbase import binariohexa
from cambiarbase import binariooctal


class test_numeracion(unittest.TestCase):
    #Binario a decimal
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

    #Decimal a binari
    def test_decimalbinario2(self):
       result =  decimalbinario(2)
       self.assertEqual(result, "10")
    def test_decimalbinario340(self):
       result =  decimalbinario(340)
       self.assertEqual(result, "101010100")  
    def test_decimalbinario5(self):
       result =  decimalbinario(5)
       self.assertEqual(result, "101") 
    def test_decimalbinario22(self):
       result =  decimalbinario(22)
       self.assertEqual(result, "10110")
    def test_decimalbinario7(self):
       result =  decimalbinario(7)
       self.assertEqual(result, "111")
    def test_decimalbinario11(self):
       result =  decimalbinario(11)
       self.assertEqual(result, "1011")

    #Decimal a hexadecimal
    def test_decimalhexa1567(self):
       result =  decitohexa(1567)
       self.assertEqual(result, "61F")   
    def test_decimalhexa15(self):
       result =  decitohexa(15)
       self.assertEqual(result, "F")   
    def test_decimalhexa1227(self):
       result =  decitohexa(1227)
       self.assertEqual(result, "4CB")   
    def test_decimalhexa100(self):
       result =  decitohexa(100)
       self.assertEqual(result, "64")   
    def test_decimalhexa10999(self):
       result =  decitohexa(10999)
       self.assertEqual(result, "2AF7")   

    #Decimal a octa
    def test_decimaloctal12(self):
       result =  decitoocta(12)
       self.assertEqual(result, "14")   
    def test_decimaloctal8(self):
       result =  decitoocta(8)
       self.assertEqual(result, "10")   
    def test_decimaloctal10999(self):
       result =  decitoocta(10999)
       self.assertEqual(result, "25367")   

    #Binario a Hexa
    def test_binariohexa27AF(self):
       result =  binariohexa("0010 0111 1010 1111")
       self.assertEqual(result, "27AF")   
    def test_binariohexa7(self):
       result =  binariohexa("0111")
       self.assertEqual(result, "7")   
    def test_binariohexa(self):
       result =  binariohexa("0001 0000 1001 1000 1011")
       self.assertEqual(result, "1098B") 

    #Binario a Octal
    def test_binariohexa27AF(self):
       result =  binariooctal("010 111 010 111")
       self.assertEqual(result, "2727")   
    def test_binariohexa7(self):
       result =  binariooctal("011 001 000")
       self.assertEqual(result, "310")   
    def test_binariohexa(self):
       result =  binariooctal("001 000 001 000 011")
       self.assertEqual(result, "10103")  

if __name__ == "__main__":
    unittest.main()
