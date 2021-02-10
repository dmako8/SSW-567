import unittest

def classifyTriangle(a,b,c):
        if (a == b and b == c):
            return 'Equilateral'

        if (a == b and b != c) or (a == c and b !=c):
            return 'Isosceles'

        if (a + b == c*c) or (a + c == b*b) or (b + c == a*a) :
            return 'Right'
       
        if (a != b) and (a!= c) and (b!= c):
            return 'Scalene'

        else :
            return 'Not a Triangle'


class ClassifyTriangle(unittest.TestCase) :
    
    def test_Equilateral(self):
        self.assertEqual(classifyTriangle(1,1,1), 'Equilateral', '(1,1,1) is Equilateral')

    def test_Isosceles(self):
        self.assertEqual(classifyTriangle(1,2,1), 'Isosceles', '(1,2,1) is Isosceles')

    def test_Scalene(self):
        self.assertEqual(classifyTriangle(7,12,15), 'Scalene', '(7,12,15) is Scalene')

    def test_Right(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right', '(3,4,5) is Right')

if __name__ == '__main__':
    # examples of running the code
    unittest.main()
