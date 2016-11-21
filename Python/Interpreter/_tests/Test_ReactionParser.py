import unittest
import numpy
import numpy.testing


from Interpreter.ReactionParser import ReactionParser


class Test_ReactionParser(unittest.TestCase):
    
    def test_Parse(self):
        template = numpy.array([
                [30,    10,     0,      0,],
                [30,    10,     0,      0,],
                [30,    10,     0,      0,],
                [30,    10,     0,      0,],
                [30,    10,     0,      0,],
                [30,    10,     0,      0,],
                [28,    10,     1,      1,],
                [28,    10,     1,      1,],
                [28,    10,     1,      1,],
                [28,    10,     1,      1,],
                [28,    10,     1,      1,],
                [29,    10,     0,      2,],
                [29,    10,     0,      2,],
                [29,    10,     0,      2,],
                [29,    10,     0,      2,],
            ])
            
        filename = 'templates/ReactionParser_Template'
        a = ReactionParser(filename)
        data = a.reaction_data
        
        numpy.testing.assert_equal(template, data)
        
        
    def test_ParseTimestep(self):
        template = numpy.array([
                [0,    0,     0,      0,],
                [0,    0,     0,      0,],
                [0,    0,     0,      0,],
                [0,    0,     0,      0,],
                [0,    0,     0,      0,],
                [-2,    0,    1,      1,],
                [0,    0,     0,      0,],
                [0,    0,     0,      0,],
                [0,    0,     0,      0,],
                [0,    0,     0,      0,],
                [1,    0,    -1,      1,],
                [0,    0,     0,      0,],
                [0,    0,     0,      0,],
                [0,    0,     0,      0,],
            ])
            
        filename = 'templates/ReactionParser_Template'
        a = ReactionParser(filename)
        data = a.ParseTimestep()
        numpy.testing.assert_equal(template, data)
        
        
        
if __name__ == '__main__':
    unittest.main()