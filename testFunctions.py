# Project 3 - Tic-Tac-Toe Simulator
#
# Name: Tyler Baxter
# Instructor: S. Einakian
# Section: 03

import unittest
from tictactoeFuncs import *


class TestCases(unittest.TestCase):
    def test_check_rows(self):
        self.assertListEqual(check_rows(["X", "X", "X", " ", " ", " ", " ", " ", " "]), [True, "X"])
        self.assertListEqual(check_rows([" ", " ", " ", "X", "X", "X", " ", " ", " "]), [True, "X"])
        self.assertListEqual(check_rows([" ", " ", " ", " ", " ", " ", "O", "O", "O"]), [True, "O"])
        self.assertListEqual(check_rows([" ", " ", " ", " ", " ", " ", " ", "O", "O"]), [False, ""])

    def test_check_cols(self):
        self.assertListEqual(check_cols(["X", " ", " ", "X", " ", " ", "X", " ", " "]), [True, "X"])
        self.assertListEqual(check_cols([" ", "X", " ", " ", "X", " ", " ", "X", " "]), [True, "X"])
        self.assertListEqual(check_cols([" ", " ", "O", " ", " ", "O", " ", " ", "O"]), [True, "O"])
        self.assertListEqual(check_cols([" ", " ", " ", " ", " ", "0", " ", " ", "O"]), [False, ""])

    def test_check_diags(self):
        self.assertListEqual(check_diags(["X", " ", " ", " ", "X", " ", " ", " ", "X"]), [True, "X"])
        self.assertListEqual(check_diags([" ", " ", "O", " ", "O", " ", "O", " ", " "]), [True, "O"])
        self.assertListEqual(check_diags([" ", " ", " ", " ", "O", " ", "O", " ", " "]), [False, ""])

    def test_board_full(self):
        self.assertEqual(board_full(["X", "X", "X", "X", "X", "X", "X", "X", "X"]), True)
        self.assertEqual(board_full(["X", "O", "O", "X", "O", "X", "O", "X", "X"]), True)
        self.assertEqual(board_full([" ", " ", " ", " ", "O", " ", "O", " ", " "]), False)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
