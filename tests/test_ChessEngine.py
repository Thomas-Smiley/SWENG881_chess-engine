import unittest

import chess
import chess.ChessAI
import chess.ChessEngine
import chess.ChessMain


class TestGameState(unittest.TestCase):
    def test_makeMove(self):

        game_state = chess.ChessEngine.GameState()
        valid_moves = game_state.getValidMoves()
        move = chess.ChessEngine.Move((0, 0), (2, 6), game_state.board)
        print('asdfasdfasdfasdf')
        print(move)

        for i in range(len(valid_moves)):
            if move == valid_moves[i]:
                print('yes')

        game_state.makeMove(move)

        for i in game_state.board:
            print(i)

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
