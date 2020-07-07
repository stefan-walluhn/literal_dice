from random import Random
from unittest import TestCase
from unittest.mock import patch

from literal_dice.literal_dice import LiteralDice
from literal_dice.tests.utils import patch_shuffle


class LiteralDiceTestCase(TestCase):
    @patch_shuffle
    def setUp(self):
        self.literal_dice = LiteralDice('HelloWorld')

    def test_object_type(self):
        self.assertIsInstance(self.literal_dice, LiteralDice)

    def test_has_word(self):
        self.assertEqual(self.literal_dice.word, 'HelloWorld')

    def test_shuffle(self):
        self.assertEqual(self.literal_dice.shuffle(), 'lrWdlloeoH')
