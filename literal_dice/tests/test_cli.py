from click.testing import CliRunner
from unittest import TestCase

from literal_dice.cli import dice
from literal_dice.tests.utils import patch_shuffle


class CliTestCase(TestCase):
    @patch_shuffle
    def setUp(self):
        self.runner = CliRunner()

    def test_cli_runs_successfully(self):
        result = self.runner.invoke(dice, ['HelloWorld'])
        self.assertEqual(0, result.exit_code)

    def test_cli_returns_shuffled_string(self):
        result = self.runner.invoke(dice, ['HelloWorld'])
        self.assertIn('lrWdlloeoH\n', result.output)

    def test_cli_number_of_shuffles(self):
        result = self.runner.invoke(dice, ['--count', 3, 'HelloWorld'])
        self.assertIn('lrWdlloeoH\nroloeHlWdl\nelWoordHll\n', result.output)
