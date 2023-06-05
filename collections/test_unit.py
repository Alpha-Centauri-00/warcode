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


    def test_even_or_odd(self):
        self.assertEqual(even_or_odd(2), "Even")
        self.assertEqual(even_or_odd(1), "Odd")
        self.assertEqual(even_or_odd(0), "Even")
        self.assertEqual(even_or_odd(1545452), "Even")
        self.assertEqual(even_or_odd(7), "Odd")
        self.assertEqual(even_or_odd(78), "Even")
        self.assertEqual(even_or_odd(17), "Odd")
        self.assertEqual(even_or_odd(74156741), "Odd")
        self.assertEqual(even_or_odd(100000), "Even")
        self.assertEqual(even_or_odd(-123), "Odd")
        self.assertEqual(even_or_odd(-456), "Even")

    
    def test_get_vowel_count(self):
        self.assertEqual(get_count("Hallo"),2)
        self.assertEqual(get_count("y"),0)
        self.assertEqual(get_count("bcdfghjklmnpqrstvwxz y"),0)
        self.assertEqual(get_count(""),0)
        self.assertEqual(get_count("abracadabra"),5)

    def test_disemvowel(self):
        self.assertEqual(disemvowel("This website is for losers LOL!"),"Ths wbst s fr lsrs LL!")
        self.assertEqual(disemvowel("No offense but,\nYour writing is among the worst I've ever read"),"N ffns bt,\nYr wrtng s mng th wrst 'v vr rd")
        self.assertEqual(disemvowel("What are you, a communist?"),"Wht r y,  cmmnst?")

    def test_aquare_didigis(self):
        self.assertEqual(square_digits(765),493625)
        self.assertEqual(square_digits(9119),811181)
        self.assertEqual(square_digits(3212),9414)

    def test_high_and_low(self):
        self.assertEqual(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"),"42 -9")
        self.assertEqual(high_and_low("1 2 3"),"3 1")
    
    def test_descending_order(self):
        self.assertEqual(descending_order(0), 0)
        self.assertEqual(descending_order(1), 1)
        self.assertEqual(descending_order(111), 111)
        self.assertEqual(descending_order(15), 51)
        self.assertEqual(descending_order(1021), 2110)
        self.assertEqual(descending_order(123456789), 987654321)

    def test_get_middle(self):
        self.assertEqual(get_middle("test"),"es")
        self.assertEqual(get_middle("testing"),"t")
        self.assertEqual(get_middle("middle"),"dd")
        self.assertEqual(get_middle("A"),"A")
        self.assertEqual(get_middle("of"),"of")

    def test_positive_sum(self):
        self.assertEqual(positive_sum([1,2,3,4,5]),15)
        self.assertEqual(positive_sum([1,-2,3,4,5]),13)
        self.assertEqual(positive_sum([-1,2,3,4,-5]),9)
        self.assertEqual(positive_sum([-1,-2,-3,-4,-5]),0)
    
    def test_is_square(self):
        self.assertEqual(is_square(-1),False)
        self.assertEqual(is_square(0),True)
        self.assertEqual(is_square(3),False)
        self.assertEqual(is_square(4),True)
        self.assertEqual(is_square(25),True)
        self.assertEqual(is_square(26),False)

if __name__ == "__main__":
    unittest.main()
