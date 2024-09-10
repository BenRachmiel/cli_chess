from Piece import *


class Game:

    def __init__(self):
        self.pieces = [[Piece() for _ in range(8)] for _ in range(8)]
        self.create_board()
        self.print_board()

    def create_board(self):

        self.pieces[0][0] = rook_0_0 = Piece("rook", 0, 0, False, 'r')
        self.pieces[0][1] = knight_0_1 = Piece("knight", 0, 1, False, 'n')
        self.pieces[0][2] = bishop_0_2 = Piece("bishop", 0, 2, False, 'b')
        self.pieces[0][3] = queen_0_3 = Piece("queen", 0, 3, False, 'q')
        self.pieces[0][4] = king_0_4 = Piece("king", 0, 4, False, 'k')
        self.pieces[0][5] = bishop_0_5 = Piece("bishop", 0, 5, False, 'b')
        self.pieces[0][6] = knight_0_6 = Piece("knight", 0, 6, False, 'n')
        self.pieces[0][7] = rook_0_7 = Piece("rook", 0, 7, False, 'r')
        self.pieces[1][0] = pawn_1_0 = Piece("pawn", 1, 0, False, 'p')
        self.pieces[1][1] = pawn_1_1 = Piece("pawn", 1, 1, False, 'p')
        self.pieces[1][2] = pawn_1_2 = Piece("pawn", 1, 2, False, 'p')
        self.pieces[1][3] = pawn_1_3 = Piece("pawn", 1, 3, False, 'p')
        self.pieces[1][4] = pawn_1_4 = Piece("pawn", 1, 4, False, 'p')
        self.pieces[1][5] = pawn_1_5 = Piece("pawn", 1, 5, False, 'p')
        self.pieces[1][6] = pawn_1_6 = Piece("pawn", 1, 6, False, 'p')
        self.pieces[1][7] = pawn_1_7 = Piece("pawn", 1, 7, False, 'p')


        self.pieces[6][0] = pawn_6_0 = Piece("pawn", 6, 0, True, 'P')
        self.pieces[6][1] = pawn_6_1 = Piece("pawn", 6, 1, True, 'P')
        self.pieces[6][2] = pawn_6_2 = Piece("pawn", 6, 2, True, 'P')
        self.pieces[6][3] = pawn_6_3 = Piece("pawn", 6, 3, True, 'P')
        self.pieces[6][4] = pawn_6_4 = Piece("pawn", 6, 4, True, 'P')
        self.pieces[6][5] = pawn_6_5 = Piece("pawn", 6, 5, True, 'P')
        self.pieces[6][6] = pawn_6_6 = Piece("pawn", 6, 6, True, 'P')
        self.pieces[6][7] = pawn_6_7 = Piece("pawn", 6, 7, True, 'P')
        self.pieces[7][0] = rook_7_0 = Piece("rook", 7, 0, True, 'R')
        self.pieces[7][1] = knight_7_1 = Piece("knight", 7, 1, True, 'N')
        self.pieces[7][2] = bishop_7_2 = Piece("bishop", 7, 2, True, 'B')
        self.pieces[7][3] = queen_7_3 = Piece("queen", 7, 3, True, 'Q')
        self.pieces[7][4] = king_7_4 = Piece("king", 7, 4, True, 'K')
        self.pieces[7][5] = bishop_7_5 = Piece("bishop", 7, 5, True, 'B')
        self.pieces[7][6] = knight_7_6 = Piece("knight", 7, 6, True, 'N')
        self.pieces[7][7] = rook_7_7 = Piece("rook", 7, 7, True, 'R')
        self.columns = ["a", "b", "c", "d", "e", "f", "g", "h"]



    def print_board(self):
        # Print the chess board in a formatted style
        print("   " + "   ".join(self.columns))
        print("  " + "----" * 8)  # Adjusted line length
        for i, row in enumerate(self.pieces):
            print(f"{8 - i} | {' | '.join(str(piece) for piece in row)} | {8 - i}")
            print("  " + "----" * 8)  # Adjusted line length
        print("   " + "   ".join(self.columns))
