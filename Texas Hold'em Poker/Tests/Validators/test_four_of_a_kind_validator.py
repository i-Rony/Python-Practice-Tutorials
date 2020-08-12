import unittest

from Poker.card import Card
from Poker.Validators import FourOfAKindValidator

class FourOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):
        self.three_of_clubs    = Card(rank = "3", suit = "Clubs")
        self.three_of_diamonds = Card(rank = "3", suit = "Diamonds")
        self.three_of_hearts   = Card(rank = "3", suit = "Hearts")
        self.three_of_spades   = Card(rank = "3", suit = "Spades")

        self.cards = [
            Card(rank = "2", suit = "Clubs"),
            self.three_of_clubs,
            self.three_of_diamonds,
            self.three_of_hearts,
            self.three_of_spades,
            Card(rank = "7", suit = "Hearts"),
            Card(rank = "9", suit = "Spades")
        ]
        
    def test_determines_that_four_cards_of_one_rank_are_present(self):
        validator = FourOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_the_four_cards_with_the_same_rank(self):
        validator = FourOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.three_of_clubs,
                self.three_of_diamonds,
                self.three_of_hearts,
                self.three_of_spades
            ]
        )
