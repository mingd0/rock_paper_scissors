from io import StringIO
import unittest
from unittest.mock import patch

from rps import Game


class TestGame(unittest.TestCase):

    def test_print_round_result_player(self):
        expected_output = "You win! Score: Player = 1, Computer = 0\n\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Game.print_round_result(self, 'player', 1, 0)
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_print_round_result_computer(self):
        expected_output = "Computer wins! Score: Player = 0, Computer = 1\n\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Game.print_round_result(self, 'computer', 0, 1)
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_print_round_result_tie(self):
        expected_output = "Tie! Score: Player = 0, Computer = 0\n\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Game.print_round_result(self, 'tie', 0, 0)
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_print_round_result_invalid_score(self):
        self.assertRaises(ValueError,
                          Game.print_round_result, self, 'computer', 0, -1)

    def test_print_round_result_invalid_player(self):
        self.assertRaises(ValueError,
                          Game.print_round_result, self, 'invalid_entry', 0, 1)

    def test_check_player_validity(self):
        self.assertRaises(ValueError,
                          Game.check_player_validity, self, 'invalid_entry')

    def test_get_score_player(self):
        gm = Game()
        self.assertEqual(gm.get_score('player'), 0)

    def test_get_score_computer(self):
        gm = Game()
        self.assertEqual(gm.get_score('computer'), 0)

    def test_get_score_invalid(self):
        gm = Game()
        self.assertRaises(ValueError, gm.get_score, 'invalid_entry')

    def test_increment_score(self):
        gm = Game()
        gm.increment_score('player')
        self.assertEqual(gm.get_score('player'), 1)

    def test_validate_player_input(self):
        self.assertTrue(Game.validatate_player_input(self, 'r'))
        self.assertTrue(Game.validatate_player_input(self, 'p'))
        self.assertTrue(Game.validatate_player_input(self, 's'))
        self.assertTrue(Game.validatate_player_input(self, 'q'))
        self.assertFalse(Game.validatate_player_input(self, 'invalid_input'))

    def test_game_logic(self):
        choices = ['r', 'p', 's']
        result = []
        expected_result = [0, -1, 1, 1, 0, -1, -1, 1, 0]
        for player_choice in choices:
            for computer_choice in choices:
                result.append(Game.game_logic(self,
                                              player_choice,
                                              computer_choice))
        self.assertEqual(result, expected_result)
        self.assertEqual(Game.game_logic(self, 'q', 's'), -999)

    def test_game_controller(self):
        gm = Game()
        gm.game_controller(1)
        gm.game_controller(1)
        gm.game_controller(0)
        gm.game_controller(-1)
        self.assertEqual(gm.get_score('player'), 2)
        self.assertEqual(gm.get_score('computer'), 1)

    def test_end_game(self):
        gm = Game()
        self.assertRaises(SystemExit, gm.end_game)


if __name__ == '__main__':
    unittest.main()
