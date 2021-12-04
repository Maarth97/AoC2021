import day1
import day2
import day3
import day4
import day5
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

# Day4 =====================================================================       
class Day4(unittest.TestCase):
    def test_check_field(self):
        inp = [[7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1],      
               [[14,21,17,24,4, 10,16,15,9,19,18,8,23,26,20,22,11,13,6,5,2,0,12,3,7]]]
        
        self.assertEqual(len(inp[1][0]) , 25)
        self.assertEqual(day4.check_field(inp[1][0], inp[0]), True)
        self.assertEqual(day4.check_field(inp[1][0], inp[0][:5]), False)
        self.assertEqual(day4.check_field(inp[1][0], inp[0][:12]), True)
        
        inp = [[7,4,9,5,11,18,23,2,0,14,10,22,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1],      
               [[14,21,17,24,4, 10,16,15,9,19,18,8,23,26,20,22,11,13,6,5,2,0,12,3,7]]]
        

        self.assertEqual(day4.check_field(inp[1][0], inp[0][:5]), False)
        self.assertEqual(day4.check_field(inp[1][0], inp[0][:12]), True)
        self.assertEqual(day4.check_field(inp[1][0], inp[0]), True)
        
        inp = [[7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1], 
               [[22,13,17,11, 0,8,2,23,4,24,21,9,14,16,7,6,10,3,18,5,1,12,20,15,19],
               [3,15,0,2,22,9,18,13,17,5,19,8,7,25,23,20,11,10,24,4,14,21,16,12,6],
               [14,21,17,24,4, 10,16,15,9,19,18,8,23,26,20,22,11,13,6,5,2,0,12,3,7]
               ]]
        
        self.assertEqual(day4.check_field(inp[1][1], inp[0]), True)
        self.assertEqual(day4.check_field(inp[1][1], inp[0][:14]), False)
        self.assertEqual(day4.check_field(inp[1][1], inp[0][:15]), True)
        
    def test_f1(self):
        inp = [[7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1], 
               [[22,13,17,11, 0,8,2,23,4,24,21,9,14,16,7,6,10,3,18,5,1,12,20,15,19],
               [3,15,0,2,22,9,18,13,17,5,19,8,7,25,23,20,11,10,24,4,14,21,16,12,6],
               [14,21,17,24,4, 10,16,15,9,19,18,8,23,26,20,22,11,13,6,5,2,0,12,3,7]
               ]]
        self.assertEqual(day4.f1(inp), 4512)
        
    def test_f2(self):
        inp = [[7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1], 
               [[22,13,17,11, 0,8,2,23,4,24,21,9,14,16,7,6,10,3,18,5,1,12,20,15,19],
               [3,15,0,2,22,9,18,13,17,5,19,8,7,25,23,20,11,10,24,4,14,21,16,12,6],
               [14,21,17,24,4, 10,16,15,9,19,18,8,23,26,20,22,11,13,6,5,2,0,12,3,7]
               ]]
        self.assertEqual(day4.f2(inp), 1924)
        
        
        
        
# Day5 =====================================================================
class Day5(unittest.TestCase):
    def test_f1(self):
        inp = []
        self.assertEqual(day5.f1(inp), 198)
        
    def test_f2(self):
        inp = []
        self.assertEqual(day5.f2(inp), 230)