import os
import unittest

from Interpreter.DataGenerator import DataGenerator


class Test_DataGenerator(unittest.TestCase, object):
    @property
    def id(self):
        return self._id
        
        
    def _MockRawInput(self, event):
        if      self.id == 0:
            self._id += 1
            return "1.0"
        elif    self.id == 1:
            self._id += 1
            return "12.0"
        elif    self.id == 2:
            self._id += 1
            return "16.0"
        else:   return None
        
        
    def __init__(self, *args, **kwargs):
        super(Test_DataGenerator, self).__init__(*args, **kwargs)
        self._id = 0
    
    
    def test__extract(self):
        original_raw_input = __builtins__.raw_input
        filename = 'templates/DataGenerator_Input'
        
        __builtins__.raw_input = self._MockRawInput
        DataGenerator(filename, 'out.data')
        __builtins__.raw_input = original_raw_input
        
        ori = open('templates/DataGenerator_Template', 'r')
        gen = open('out.data', 'r')
        
        ori_data = ori.readlines()
        gen_data = gen.readlines()
        
        self.assertTrue(len(ori_data) == len(gen_data))
        
        total = len(ori_data)
        
        for i in xrange(total):
            self.assertMultiLineEqual(ori_data[i], gen_data[i], msg="Fail in line %i" %i)
        
        
        ori.close()
        gen.close()
        
        os.remove('out.data')
        



if __name__ == '__main__':
    unittest.main()
        
        
        
        