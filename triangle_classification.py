'''This file is for defining the triangle classification problem

Reference code: 10.1109/CONFLUENCE.2016.7508052
'''

class Triangle:
    '''Class for the Triangle figure'''
    def __init__(self, a: float, b: float, c: float) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.classification = self.__classify()

    def get_classification(self) -> str:
        '''Gets the triangle classification'''
        return self.classification

    def __classify(self) -> str:
        '''Classifies the triangle'''
        classification = None

        if self.a > 0 and self.b > 0 and self.c > 0:
            if self.a+self.b > self.c and self.b+self.c > self.a and self.c+self.a > self.b:
                if self.a != self.b and self.b != self.c and self.c != self.a:
                    classification = 'scalene'
                elif self.a == self.b and self.b == self.c:
                    classification = 'equilateral'
                elif ((self.a == self.b and self.a != self.c) or
                      (self.a == self.c and self.a != self.b) or
                      (self.b == self.c and self.b != self.a)):
                    classification = 'isosceles'
            else:
                classification = 'invalid'
        else:
            classification = 'out of range'

        return classification
