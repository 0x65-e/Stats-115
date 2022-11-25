import sys
sys.path.append('../src/')

import unittest
from ddt import ddt, data, unpack
import forward_YourLastName_YourFirstName as targetCode #change to file name


@ddt
class TestForward(unittest.TestCase):
    
    def assertNumericDictAlmostEqual(self, calculatedDictionary, expectedDictionary, places=7):
        self.assertEqual(calculatedDictionary.keys(), expectedDictionary.keys())
        for key in calculatedDictionary.keys():
            self.assertAlmostEqual(calculatedDictionary[key], expectedDictionary[key], places=places)

##################################################
#		Complete the code below
##################################################  
                
    @data()#(xT_1Distribution, eT, transitionTable, sensorTable, expectedResult)
    @unpack
    def test_forward(self, xT_1Distribution, eT, transitionTable, sensorTable, expectedResult):
        
        
        
        self.assertNumericDictAlmostEqual(calculatedResult, expectedResult, places=4)

##################################################
#		Complete the code above
##################################################  
	
    def tearDown(self):
       pass
 
if __name__ == '__main__':
    unittest.main(verbosity=2)