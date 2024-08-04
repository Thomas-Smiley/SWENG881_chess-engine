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


if __name__ == '__main__':
    unittest.main()
