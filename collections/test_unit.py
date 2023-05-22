from typing import Any
import unittest
from main import *


class TestMulbyN(unittest.TestCase):

    def test_mul_by_n(self):
        
        self.assertEqual(mul_by_n([1, 2, 3], 4), [4, 8, 12])
        self.assertEqual(mul_by_n([9, 1], 9), [81, 9])
        self.assertEqual(mul_by_n([5, 5, 5, 5, 5], 1), [5, 5, 5, 5, 5])
        self.assertEqual(mul_by_n([5, 5, 5, 5, 5], 2), [10, 10, 10, 10, 10])
        self.assertEqual(mul_by_n([77, 88], 0), [0, 0])


    def test_compaer(self):
        self.assertEqual(compare(10, 11), "50%")
        self.assertEqual(compare(45, 45), "100%")
        self.assertEqual(compare(29, 92), "100%")
        self.assertEqual(compare(14, 24), "50%")
        self.assertEqual(compare(56, 57), "50%")
        self.assertEqual(compare(38, 84), "50%")
        self.assertEqual(compare(10, 22), "0%")
        self.assertEqual(compare(11, 44), "0%")
        self.assertEqual(compare(98, 70), "0%")
        self.assertEqual(compare(66, 16), "50%")
        self.assertEqual(compare(98, 88), "50%")
        self.assertEqual(compare(78, 58), "50%")
        self.assertEqual(compare(47, 56), "0%")

        # Additional test cases
        self.assertEqual(compare(0, 0), "100%")  # Both numbers are zero
        self.assertEqual(compare(123, 0), "0%")  # Second number is zero
        self.assertEqual(compare(0, 123), "0%")  # First number is zero
        self.assertEqual(compare(1111, 222), "0%")  # No matching digits

    def test_alternate(self):
        self.assertEqual(alternate(5,True,False), [True,False,True,False,True])
        self.assertEqual(alternate(5,"True","False"), ["True","False","True","False","True"])
        self.assertEqual(alternate(20,"red","blue"), ["red","blue","red","blue","red","blue","red","blue","red","blue","red","blue","red","blue","red","blue","red","blue","red","blue"])
        self.assertEqual(alternate(0,"lemons","ornge"), [])
            


    def test_name_shuffler(self):
        self.assertEqual(name_shuffler('john McClane'),'McClane john')
        self.assertEqual(name_shuffler('Mary jeggins'),'jeggins Mary')
        self.assertEqual(name_shuffler('tom jerry'),'jerry tom')


    def test_set_reducer(self):
        self.assertEqual(set_reducer([0, 4, 6, 8, 8, 8, 5, 5, 7]), 2)
        self.assertEqual(set_reducer([8, 1, 6, 1, 2, 7, 7, 7, 7, 6, 5, 3, 2, 1, 8]), 3)
        self.assertEqual(set_reducer([0, 0, 8, 6, 6, 7, 8, 6, 6, 4, 7, 6, 4, 0, 1, 1, 2, 1, 2, 9, 9, 0, 3, 3, 0, 4]), 2)
        self.assertEqual(set_reducer([6, 3, 5, 7, 4, 2, 0, 0, 1, 6, 9, 6, 1, 3, 9, 3, 2]), 3)
        self.assertEqual(set_reducer([1, 4, 0, 1, 2, 6, 6, 0, 8, 4, 7, 9, 9, 4, 3, 7, 2, 6, 7, 5, 0, 9, 8]), 5)
        self.assertEqual(set_reducer([4, 6, 8, 1, 9, 3, 8, 4, 1, 4, 0, 8, 3, 7, 1, 5, 6, 3, 2, 1, 8, 4, 9]),23)
        self.assertEqual(set_reducer([8, 3, 2, 6, 2, 7, 9, 9, 6, 8, 2, 4, 3, 6, 9, 5, 2, 4, 9]),3)
        self.assertEqual(set_reducer([7, 2, 0, 6, 5, 7, 3, 9, 1, 8, 4, 5, 5, 5, 8, 9, 8, 1, 9, 1, 2, 7, 2, 6, 0, 8, 0, 2]),3)
        self.assertEqual(set_reducer([8, 5, 1, 1, 1, 5, 9, 7, 4, 8, 8, 8, 2, 4, 3, 1, 2, 1, 3, 5, 6, 4]),5)
        self.assertEqual(set_reducer([2, 4, 4, 6, 2, 1, 1, 5, 6, 7, 8, 8, 8, 8, 9, 0, 1, 1, 5, 4, 4]),3)
    

    def test_validate_hello(self):
        self.assertEqual(validate_hello("hello"),True)
        self.assertEqual(validate_hello("ciao bella!"),True)
        self.assertEqual(validate_hello("salut"),True)
        self.assertEqual(validate_hello("hallo, salut"),True)
        self.assertEqual(validate_hello("hombre! Hola!"),True)
        self.assertEqual(validate_hello("Hallo, wie geht\'s dir?"),True)
        self.assertEqual(validate_hello("AHOJ!"),True)
        self.assertEqual(validate_hello("czesc"),True)
        self.assertEqual(validate_hello("meh"),False)
        self.assertEqual(validate_hello("Ahoj"),True)
        self.assertEqual(validate_hello("bla"),False)
        self.assertEqual(validate_hello("good morning"),False)

    def test_find_avarage(self):
        self.assertEqual(find_average([2,4,6]),4)
        self.assertEqual(find_average([1,2,3]),2)


    def test_paperwork(self):
        self.assertEqual(paperwork(5,5),25)
        self.assertEqual(paperwork(-5,5),0)
        self.assertEqual(paperwork(5,-5),0)
        self.assertEqual(paperwork(-5,-5),0)

    
    def test_domain_name(self):
        self.assertEqual(domain_name("https://google.com"), "google")
        self.assertEqual(domain_name("http://google.co.jp"), "google")
        self.assertEqual(domain_name("www.xakep.com"), "xakep")
        self.assertEqual(domain_name("www.youtube.com"), "youtube")
        self.assertEqual(domain_name("https://youtube.com"), "youtube")


    def test_instence_of_class(self):
        g = Python("Bubba")
        self.assertEqual(g.name,"Bubba",f"A class should be Called {g.name}!!!!")

if __name__ == "__main__":
    unittest.main()