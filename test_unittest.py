import day1
import day2
import day3
import unittest

# Day1 =====================================================================
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
        
# Day2 =====================================================================
class Day2(unittest.TestCase):
    def test_f1(self):
        inp = ["forward 5",
                "down 5",
                "forward 8",
                "up 3",
                "down 8",
                "forward 2"]
        self.assertEqual(day2.f1(inp), 150)
        
    def test_f2(self):
        inp = ["forward 5",
                "down 5",
                "forward 8",
                "up 3",
                "down 8",
                "forward 2"]
        self.assertEqual(day2.f2(inp), 900)
        
# Day3 =====================================================================
class Day3(unittest.TestCase):
    def test_f1(self):
        inp = ["00100",
                "11110",
                "10110",
                "10111",
                "10101",
                "01111",
                "00111",
                "11100",
                "10000",
                "11001",
                "00010",
                "01010"]
        self.assertEqual(day3.f1(inp), 198)
        
    def test_f2(self):
        inp = ["00100",
                "11110",
                "10110",
                "10111",
                "10101",
                "01111",
                "00111",
                "11100",
                "10000",
                "11001",
                "00010",
                "01010"]
        self.assertEqual(day3.f2(inp), 230)