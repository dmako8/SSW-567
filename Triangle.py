import unittest

def classifyTriangle(a,b,c):

    
        
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput'
      
       # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

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
