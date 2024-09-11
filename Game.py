from Piece import *
import re




class Game:
    # constractor
    def __init__(self):
        self.pieces = [[Piece() for _ in range(8)] for _ in range(8)]
        self.create_board()
        self.print_board()

    # game process is a function that responsible for the order of the game, and it calls the necessary functions to
    # run the game
    def game_process(self):
        white_player = input("enter white's player name")
        black_player = input("enter black's player name")
        while True:
            white_algebraic_notation = input("white's turn")  # getting the user algebraic_notation input from the cli
            if self.check_input(white_algebraic_notation):
                # calling check_input to make sure data is in the correct format

                piece = find_piece_object_through_algebraic_notation(algebraic_notation)  #
                dest_location =  check_selected_object_is_a_peace(piece)
                if check_move_is_possible(piece, white_algebraic_notation) == True:

                    move_piece(piece, white_algebraic_notation)

            black_move = input("black's turn")

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

    def check_input(self, input_from_user):
        regex_pattern = r"""
                     ^(?:  
                        [KQRBN]?[a-h][1-8]           
                        |
                        [KQRBN]?[a-h]?x[a-h][1-8]             
                        | 
                        [KQRBN]?[a-h][1-8]\+                  
                        |
                        [KQRBN]?[a-h][1-8]\#                  
                        |                                    
                        [a-h]x[a-h][1-8] ep                  
                    )$
                """
        return bool(re.match(regex_pattern, str(input_from_user), re.VERBOSE))

    def move_input(self):
        # בדיקת חוקיות המהלך

        move = input("enter move")

        if self.check_input(move):
            print("המהלך חוקי לפי הסימון האלגברי.")
        else:
            print("המהלך לא חוקי לפי הסימון האלגברי.")

    # מהלך לפי סימון אלגברי (לדוגמה, Qxe4, exd5, או Qd4+):

    def find_piece_object_through_algebraic_notation(self,algibraic_notation):





