import day1
import unittest

# Day1
class Day1(unittest.TestCase):
    def test_count_increase(self):
        self.assertEqual(day1.count_increase([0,1,2,3]), 3)
        self.assertEqual(day1.count_increase([0,1,2,1,3,4,5]), 5)
        
        inp = [199,200,208,210,200,207,240,269,260,263]
        self.assertEqual(day1.count_increase(inp), 7)
        
    def test_count_increase_triples(self):
        self.assertEqual(day1.count_increase_triples([0,1,2,1]), 1)
        self.assertEqual(day1.count_increase_triples([0,1,2,1,2,1]), 2)
        
        inp = [199,200,208,210,200,207,240,269,260,263]
        self.assertEqual(day1.count_increase_triples(inp), 5)
        

