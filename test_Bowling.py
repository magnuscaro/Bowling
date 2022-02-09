from cmath import exp
import Bowling
import unittest

class TestBowlingGame(unittest.TestCase):
    
    def test_griefBowlingResults(self):
        Rolls = ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']
        Game = Bowling.bowlingGame(Rolls)
        Game.calculateScore()
        actualScore = Game.getScore()
        expectedScore = 20
        self.assertEqual(expectedScore, actualScore)
    
    def test_StrikeBowlingResults(self):
        Rolls = ['X','X','X','X','X','X','X','X','X','X','X','X']
        Game = Bowling.bowlingGame(Rolls)
        Game.calculateScore()
        actualScore = Game.getScore()
        expectedScore = 300
        self.assertEqual(expectedScore, actualScore)
    
    def test_RegularBowlingResults(self):
        Rolls = ['9','-','9','-','9','-','9','-','9','-','9','-','9','-','9','-','9','-','9','-']
        Game = Bowling.bowlingGame(Rolls)
        Game.calculateScore()
        actualScore = Game.getScore()
        expectedScore = 90
        self.assertEqual(expectedScore, actualScore)

    def test_SpareBowlingResults(self):
        Rolls = ['5','/','5','/','5','/','5','/','5','/','5','/','5','/','5','/','5','/','5','/','5']
        Game = Bowling.bowlingGame(Rolls)
        Game.calculateScore()
        actualScore = Game.getScore()
        expectedScore = 150
        self.assertEqual(expectedScore, actualScore)
    
    def test_RandomBowlingResults(self):
        Rolls = ['1','1','3','4','5','/','2','2','3','3','5','/','2','1','4','/','3','2','1','1']
        Game = Bowling.bowlingGame(Rolls)
        Game.calculateScore()
        actualScore = Game.getScore()
        expectedScore = 66
        self.assertEqual(expectedScore, actualScore)

    def test_RandomBowlingResults2(self):
        Rolls = ['4','4','6','/','7','/','X','8','/','1','5','6','/','3','5','X','8','/','X']
        Game = Bowling.bowlingGame(Rolls)
        Game.calculateScore()
        actualScore = Game.getScore()
        expectedScore = 143
        self.assertEqual(expectedScore, actualScore)

    def test_RandomBowlingResults3(self):
        Rolls = ['1','1','X','9','/','1','1','1','1','1','1','1','1','1','1','1','1','1','1']
        Game = Bowling.bowlingGame(Rolls)
        Game.calculateScore()
        actualScore = Game.getScore()
        expectedScore = 47
        self.assertEqual(expectedScore, actualScore)

if __name__ == '__main__':
    unittest.main()

