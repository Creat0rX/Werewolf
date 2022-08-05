import unittest
import winConditions

class TestStringMethods(unittest.TestCase):

    def testTownWins(self):
        self.assertEqual(winConditions.winCondition(["Werewolf"]), 'Town Wins!!!')

    def testWerewolfWins(self):
        self.assertEqual(winConditions.winCondition(["Drunk"]), 'Werewolfs Wins!!!')

    def testNeutralWins(self):
        self.assertEqual(winConditions.winCondition(["Tanner"]), 'Tanner Wins!!!')


if __name__ == '__main__':
    unittest.main()