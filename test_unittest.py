import unittest

import Puzzles.day1 as day1
import Puzzles.day2 as day2
import Puzzles.day3 as day3
import Puzzles.day4 as day4
import Puzzles.day5 as day5
import Puzzles.day6 as day6
import Puzzles.day7 as day7
import Puzzles.day8 as day8
import Puzzles.day9 as day9
import Puzzles.day10 as day10
import Puzzles.day11 as day11
import Puzzles.day12 as day12
import Puzzles.day13 as day13
import Puzzles.day14 as day14
import Puzzles.day15 as day15
#import Puzzles.day16 as day16
#import Puzzles.day17 as day17
#import Puzzles.day18 as day18
#import Puzzles.day19 as day19
#import Puzzles.day20 as day20
#import Puzzles.day21 as day21
#import Puzzles.day22 as day22
#import Puzzles.day23 as day23
#import Puzzles.day24 as day24
#import Puzzles.day25 as day25




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
        inp = """0,9 -> 5,9
                8,0 -> 0,8
                9,4 -> 3,4
                2,2 -> 2,1
                7,0 -> 7,4
                6,4 -> 2,0
                0,9 -> 2,9
                3,4 -> 1,4
                0,0 -> 8,8
                5,5 -> 8,2""".splitlines()
        self.assertEqual(day5.f1(inp), 5)
        
    def test_f2(self):
        inp = """0,9 -> 5,9
                8,0 -> 0,8
                9,4 -> 3,4
                2,2 -> 2,1
                7,0 -> 7,4
                6,4 -> 2,0
                0,9 -> 2,9
                3,4 -> 1,4
                0,0 -> 8,8
                5,5 -> 8,2""".splitlines()
        self.assertEqual(day5.f2(inp), 12)
        
# Day6 =====================================================================
class Day6(unittest.TestCase):
    def test_f1(self):
        inp = [3,4,3,1,2]
        self.assertEqual(day6.f1(inp, NUM_DAYS = 18), 26)
        self.assertEqual(day6.f1(inp, NUM_DAYS = 80), 5934)
        
    def test_f2(self):
        inp = [3,4,3,1,2]
        self.assertEqual(day6.f2(inp, NUM_DAYS = 18), 26)
        self.assertEqual(day6.f2(inp, NUM_DAYS = 80), 5934)
        self.assertEqual(day6.f2(inp, NUM_DAYS = 256), 26984457539)
        
# Day7 =====================================================================
class Day7(unittest.TestCase):
    def test_f1(self):
        inp = [16,1,2,0,4,2,7,1,2,14]
        self.assertEqual(day7.f1(inp),37)

        
    def test_f2(self):
        inp = [16,1,2,0,4,2,7,1,2,14]
        self.assertEqual(day7.f2(inp), 168)

# Day8 =====================================================================
class Day8(unittest.TestCase):
    def test_f1(self):
        inp = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |fgae cfgab fg bagce""".splitlines()
      
        self.assertEqual(day8.f1(inp),26)

        
    def test_f2(self):
        inp = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |fgae cfgab fg bagce""".splitlines()
      
        self.assertEqual(day8.f2(inp), 61229)
        

# Day9 =====================================================================
class Day9(unittest.TestCase):
    def test_f1(self):
        inp = [[int(y) for y in x.replace("\n","")] for x  in """2199943210
3987894921
9856789892
8767896789
9899965678""".splitlines()]
        self.assertEqual(day9.f1(inp),15)

        
    def test_f2(self):
        inp = [[int(y) for y in x.replace("\n","")] for x  in """2199943210
3987894921
9856789892
8767896789
9899965678""".splitlines()]
        self.assertEqual(day9.f2(inp), 1134)
        
# Day10 =====================================================================
class Day10(unittest.TestCase):
    inp = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]""".splitlines()

    def test_f1(self):
        self.assertEqual(day10.f1(self.inp), 26397)


        
    def test_f2(self):

        self.assertEqual(day10.f2(self.inp), 288957)
        
# Day11 =====================================================================
class Day11(unittest.TestCase):
    inp = [[int(y) for y in x.replace("\n","")] for x  in """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526""".splitlines()]

    def test_f1(self):
        self.assertEqual(day11.f1(self.inp), 1656)


        
    def test_f2(self):
        self.assertEqual(day11.f2(self.inp), 195)
        
# Day12 =====================================================================
class Day12(unittest.TestCase):
    
    convert = lambda data: [x.replace("\n","").strip().split("-") for x in data]
    
    inp = convert("""start-A
    start-b
    A-c
    A-b
    b-d
    A-end
    b-end""".splitlines())
    
    inp2 = convert("""dc-end
    HN-start
    start-kj
    dc-start
    dc-HN
    LN-dc
    HN-end
    kj-sa
    kj-HN
    kj-dc""".splitlines())
    

    def test_f1(self):
        self.assertEqual(day12.f1(self.inp), 10)
        self.assertEqual(day12.f1(self.inp2), 19)

        
    def test_f2(self):
        self.assertEqual(day12.f2(self.inp), 36)
        self.assertEqual(day12.f2(self.inp2), 103)
        
        
        
# Day13 =====================================================================
class Day13(unittest.TestCase):
    
    convert = lambda data: [x.replace("\n","").strip().split("-") for x in data]
    
    inp = ([[6,10],
[0,14],
[9,10],
[0,3],
[10,4],
[4,11],
[6,0],
[6,12],
[4,1],
[0,13],
[10,12],
[3,4],
[3,0],
[8,4],
[1,10],
[2,14],
[8,10],
[9,0]],

[["y",7],
["x",5]])

    def test_f1(self):
        self.assertEqual(day13.f1(self.inp), 17)
        
    def test_f2(self):
        self.assertEqual(day13.f2(self.inp), 16)


# Day14 =====================================================================
class Day14(unittest.TestCase):
    
    RAW = "NNCB","""CH -> B
    HH -> N
    CB -> H
    NH -> C
    HB -> C
    HC -> B
    HN -> C
    NN -> C
    BH -> H
    NC -> B
    NB -> B
    BN -> B
    BB -> N
    BC -> B
    CC -> N
    CN -> C""".splitlines()

    convert = lambda x: [[a for a in ele.strip().split(" -> ")] for ele in x]       
    inp = RAW[0], convert(RAW[1])  

    def test_f1(self):
        self.assertEqual(day14.f1(self.inp), 1588)
        
    def test_f2(self):
        self.assertEqual(day14.f2(self.inp), 2188189693529)


# Day15 =====================================================================
class Day15(unittest.TestCase):
    
    inp = []

    def test_f1(self):
        self.assertEqual(day15.f1(self.inp), None)
        
    def test_f2(self):
        self.assertEqual(day15.f2(self.inp), None)
