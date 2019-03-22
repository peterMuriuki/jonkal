import unittest
from unittest.mock import patch
from interface import Board, create_board, prompt

class BoardTest(unittest.TestCase):
    """Verifies the internal representational structure of the board
    is as it should be ; also tests utility functions that are involved
    in creating a board although not directly part of the board"""
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_underlying_representation(self):
        """
        for variable values of bowls and number of beads, make
        sure the representaion is correct
        """
        board = Board(3, 5)
        self.assertIsInstance(board.bowls, list)
        self.assertEqual(board.bowls[len(board.bowls) // 2].type, 'Nest')
        for index in range(12):
            if index % 5 != 0:
                self.assertEqual(board.bowls[index].beads, 3)
                self.assertEqual(board.bowls[index].type, 'Bowl')
            else:
                self.assertEqual(board.bowls[index].beads, 0)
                self.assertEqual(board.bowls[index].type, 'Nest')

    def test_re_underlying_representation(self):
        """
        for variable values of bowls and number of beads, make
        sure the representaion is correct
        """
        board = Board(6, 7) # 7 bowls with 6 beads per bowl
        for index in range(16):
            if index % 7 != 0:
                self.assertEqual(board.bowls[index].beads, 3)
                self.assertEqual(board.bowls[index].type, 'Bowl')
            else:
                self.assertEqual(board.bowls[index].beads, 0)
                self.assertEqual(board.bowls[index].type, 'Nest')

    def test_repr(self):
        """check if we have errors in serializing object to string"""
        self.assertIsInstance(repr(Board(3)), str)
        self.assertIsInstance(repr(Board(3, 7)), str)

    def test__prompt_method(self):
        with patch('builtins.input', return_value=1):
            self.assertTrue(prompt('some prompt'), range(1, 5))

    def test_create_board_factory_method(self):
        with patch('prompt', return_value=4):
            board = create_board()
            self.assertEqual(board.bowls[0].beads, 4)
