import unittest

from Poker.card import Card
from Poker.Validators import RoyalFlushValidator

class RoyalFlushValidatorTest(unittest.TestCase):
    def test_validates_that_cards_do_not_have_straight_flush_ending_in_ace(self):
        cards = [
            Card(rank = "9", suit = "Clubs"),
            Card(rank = "10", suit = "Clubs"),
            Card(rank = "Jack", suit = "Clubs"),
            Card(rank = "Queen", suit = "Clubs"),
            Card(rank = "King", suit = "Clubs"),
            Card(rank = "Ace", suit = "Diamonds")
        ]

        validator = RoyalFlushValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            False
        )

    def test_validates_that_cards_do_not_have_straight_flush_ending_in_ace(self):
        cards = [
            Card(rank = "2", suit = "Spades"),
            Card(rank = "10", suit = "Clubs"),
            Card(rank = "Jack", suit = "Clubs"),
            Card(rank = "Queen", suit = "Clubs"),
            Card(rank = "King", suit = "Clubs"),
            Card(rank = "Ace", suit = "Clubs"),
            Card(rank = "Ace", suit = "Diamonds")
        ]

        validator = RoyalFlushValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_five_straight_cards_with_same_rank_ending_in_ace(self):
        ten   = Card(rank = "10", suit = "Clubs")
        jack  = Card(rank = "Jack", suit = "Clubs")
        queen = Card(rank = "Queen", suit = "Clubs")
        king  = Card(rank = "King", suit = "Clubs")
        ace   = Card(rank = "Ace", suit = "Clubs")

        cards = [
            Card(rank = "2", suit = "Spades"),
            ten,
            jack,
            queen,
            king,
            ace,
            Card(rank = "Ace", suit = "Diamonds")
        ]

        validator = RoyalFlushValidator(cards = cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                ten,
                jack,
                queen,
                king,
                ace
            ]
        )
