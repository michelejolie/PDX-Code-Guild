import unittest
#need to add import file test

class TestCard(unittest.TestCase):
    def setup(self):
        self.card1 = Card('Ace', 'Diamonds', 1)
        self.card1 = Card('10', 'Hearts', 10)
        self.player = Hand()
        self.player = Hit(self.card1)
        self.player = Hit(self.card2)

    def test_value(self):
        self.assertEqual(self.card1.value, 1)
        self.assertEqual(self.card2.value, 10)

    def test_hand(self):
        self.assertEqual(self.player.score_hand(), 21)

    def test_hand_hit(self):
        self.assertEqual(len(self.player.hand(), 2))
if __name__ == '__main__':
    unittest.main()