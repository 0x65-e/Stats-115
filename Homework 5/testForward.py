import sys
sys.path.append('../src/')

import unittest
from ddt import ddt, data, unpack
import forward as targetCode


@ddt
class TestForward(unittest.TestCase):
    
    def assertNumericDictAlmostEqual(self, calculatedDictionary, expectedDictionary, places=7):
        self.assertEqual(calculatedDictionary.keys(), expectedDictionary.keys())
        for key in calculatedDictionary.keys():
            self.assertAlmostEqual(calculatedDictionary[key], expectedDictionary[key], places=places)
                
    @data(({0: 0.435, 1: 0.278, 2: 0.287}, 0, {0: {0: 0.423, 1: 0.333, 2: 0.244}, 1: {0: 0.065, 1: 0.216, 2: 0.719}, 2: {0: 0.423, 1: 0.145, 2: 0.432}}, {0: {0: 0.05, 1: 0.95}, 1: {0: 0.4, 1: 0.6}, 2: {0: 0.85, 1: 0.15}}, {0: 0.0336753447580515, 1: 0.20530929377302407, 2: 0.7610153614689245}), ({0: 0.513, 1: 0.343, 2: 0.144}, 0, {0: {0: 0.262, 1: 0.488, 2: 0.250}, 1: {0: 0.659, 1: 0.178, 2: 0.163}, 2: {0: 0.376, 1: 0.352, 2: 0.272}}, {0: {0: 0.85, 1: 0.15}, 1: {0: 0.25, 1: 0.75}, 2: {0: 0.30, 1: 0.70}}, {0: 0.6910887042646321, 1: 0.1775214884808564, 2: 0.13138980725451152})) #(xT_1Distribution, eT, transitionTable, sensorTable, expectedResult)
    @unpack
    def test_forward(self, xT_1Distribution, eT, transitionTable, sensorTable, expectedResult):
        calculatedResult = targetCode.forward(xT_1Distribution, eT, transitionTable, sensorTable)
        self.assertNumericDictAlmostEqual(calculatedResult, expectedResult, places=4)
	
    def tearDown(self):
       pass
 
if __name__ == '__main__':
    unittest.main(verbosity=2)