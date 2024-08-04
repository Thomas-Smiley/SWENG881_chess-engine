import unittest

import chess
import chess.ChessAI
import chess.ChessEngine
import chess.ChessMain


class TestGameState(unittest.TestCase):
    def test_makeMove(self):

        game_state = chess.ChessEngine.GameState()
        valid_moves = game_state.getValidMoves()
        move = chess.ChessEngine.Move((6, 0), (4, 0), game_state.board)
        print(move)

        for i in range(len(valid_moves)):
            if move == valid_moves[i]:
                game_state.makeMove(valid_moves[i])

        self.assertEqual(game_state.board, [['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
                                            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
                                            ['--', '--', '--', '--', '--', '--', '--', '--'],
                                            ['--', '--', '--', '--', '--', '--', '--', '--'],
                                            ['wp', '--', '--', '--', '--', '--', '--', '--'],
                                            ['--', '--', '--', '--', '--', '--', '--', '--'],
                                            ['--', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
                                            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']])

        for i in game_state.board:
            print(i)

        self.assertEqual(True, True)

    def test_notInCheck(self):
        game_state = chess.ChessEngine.GameState()
        valid_moves = game_state.getValidMoves()

        self.assertEqual(game_state.inCheck(), False)

    def test_inCheck(self):
        game_state = chess.ChessEngine.GameState()
        game_state.board = [['--', '--', '--', 'bQ', 'bK', '--', '--', '--'],
                            ['--', '--', '--', '--', '--', '--', '--', '--'],
                            ['--', '--', '--', '--', '--', '--', '--', '--'],
                            ['--', '--', '--', '--', '--', '--', '--', '--'],
                            ['--', '--', '--', '--', '--', '--', '--', '--'],
                            ['--', '--', '--', '--', '--', '--', '--', '--'],
                            ['--', '--', '--', '--', '--', '--', '--', '--'],
                            ['--', '--', '--', 'wK', '--', '--', '--', '--']]
        game_state.white_to_move = True
        valid_moves = game_state.getValidMoves()
        self.assertEqual(game_state.inCheck(), True)

        game_state.white_to_move = False
        valid_moves = game_state.getValidMoves()
        self.assertEqual(game_state.inCheck(), False)


if __name__ == '__main__':
    unittest.main()
