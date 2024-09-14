from Piece import *
import re


class Game:
    # constractor
    def __init__(self):
        self.current_turn = "White"
        self.pieces = [[Piece() for _ in range(8)] for _ in range(8)]
        self.create_board()
        self.print_board()
        self.game_process()

    # game process is a function that responsible for the order of the game, and it calls the necessary functions to
    # run the game
    def game_process(self):
        white_player = input("Enter white's player name: ")
        black_player = input("Enter black's player name: ")
        while True:
            algebraic_notation = input(
                f"{self.current_turn}'s turn: ")  # getting the user algebraic_notation input from the cli

            if not self.move_input(algebraic_notation):
                print("Invalid algebraic notation. Please try again.")
                continue  # This will start the loop over

            piece_and_destination = self.create_object_and_dest_tuple_through_algebraic_notation(algebraic_notation)

            if not self.selected_object_isnt_empty(piece_and_destination[0]):
                print("You chose an empty object. Please try again.")
                continue

            if not self.check_move_piece_sync(piece_and_destination):
                print("Invalid move for this piece. Please try again.")
                continue

            if not self.check_clear_path():
                print("The path is not clear. Please try again.")
                continue

            # If we've made it this far, the move is valid
            self.move_piece(piece_and_destination)  # calls out check_if_takes()
            if self.check_if_check():
                # limit movements as required
                pass
            if self.current_turn == "White":
                self.current_turn = "Black"
            else:
                self.current_turn = "White"

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

    def move_input(self, move):
        # בדיקת חוקיות המהלך

        if self.check_input(move):
            print("המהלך חוקי לפי הסימון האלגברי.")
            return True
        else:
            print("המהלך לא חוקי לפי הסימון האלגברי.")
            return False

    # מהלך לפי סימון אלגברי (לדוגמה, Qxe4, exd5, או Qd4+):

    def create_object_and_dest_tuple_through_algebraic_notation(self, algebraic_notation):
        # Extracting destination indices from algebraic notation (e.g., 'h7')
        raw_dest_x_y = algebraic_notation[-2:]
        array_dest_x_y = self.chess_position_to_indices(raw_dest_x_y)

        # Extracting the chosen piece based on the length of the algebraic notation
        piece = Piece()
        y = piece.y
        match len(algebraic_notation):
            case 2:
                # Handle simple moves (e.g., 'h7')
                # column for find)piece_in_column func
                column = ord(algebraic_notation[0].lower()) - 97  # Convert letter to column index
                if self.current_turn == "White":
                    # capturing specific pawn object.
                    piece = self.find_piece_in_column(column, "pawn", True)
                    # casting pawn values to send them to move_object.
                    start_position = (piece.x, piece.y)
                    # start_position = self.convert_2d_array_indices_into_chess(str((piece.x, piece.y)))

                    end_position = self.chess_position_to_indices(algebraic_notation)
                    self.move_piece(start_position, end_position)
                else:
                    piece = self.find_piece_in_column(column, "pawn", False)

            case 3:
                # Handle moves with captures or special cases (e.g., 'Nxe5')
                # Implement custom logic based on the algebraic notation
                pass

            case 4:
                # Handle castling or promotion (e.g., 'e8=Q')
                pass

            case 5:
                # Handle more complex moves (e.g., 'exf6+')
                pass

        # Create the tuple with the piece and destination indices
        piece_and_destination_tuple = (piece.x, piece.y, array_dest_x_y)
        print(piece_and_destination_tuple)
        return piece_and_destination_tuple

    def find_piece_in_column(self, column, piece_type, is_white):
        for row, piece in enumerate(self.iterate_column(column)):
            if piece and piece.type == piece_type and piece.is_big == is_white:
                return piece
        return None

    def iterate_column(self, column):
        for row in range(7, -1, -1):  # Start from the bottom (row 7) to the top (row 0)
            yield self.pieces[row][column]

    def selected_object_isnt_empty(self, piece):
        pass

    def extracting_index_of_dest(self, algebraic_notation):
        return algebraic_notation

    def chess_position_to_indices(self, pos):
        # מיפוי האותיות לעמודות (ציר X)
        column = ord(pos[0].lower()) - ord('a')

        # מיפוי המספרים לשורות (ציר Y)
        row = 8 - int(pos[1])

        return row, column

    def chess_position_to_column(pos):
        # מיפוי האותיות לעמודות (ציר X)
        column = ord(pos[0].lower()) - ord('a')

        return column

    def finding_specific_piece(self, algebraic_notation):
        for piece in iterate_column(chess_board, 4):
            pass

    def chess_position_to_index(self, position):
        """
        Converts a chess position (e.g., 'e2') to 2D array indices.
        """
        column = position[0]
        row = position[1]

        # Convert column letter to index (a=0, b=1, ..., h=7)
        column_index = ord(column.lower()) - ord('a')

        # Convert row number to index (1=7, 2=6, ..., 8=0)
        row_index = 8 - int(row)

        return row_index, column_index

    def move_piece(self, start_position, end_position):
        # Get user input for the starting and target positions

        # Convert chess positions to array indices
        start_row, start_col = start_position
        end_row, end_col = end_position

        # Get the piece at the starting position
        current_piece = self.pieces[start_row][start_col]

        # If there's no piece at the starting position, the move is invalid
        if current_piece is None:
            print("No piece at the starting position.")
            return

        # Get the piece at the target position (if any)
        target_piece = self.pieces[end_row][end_col]

        # You can add logic here to check if the move is legal based on the piece type
        print(f"{current_piece} moves to {end_position}")

        # Update the board: Create a new tuple with the updated positions
        pieces_list = [list(row) for row in self.pieces]  # Create a copy of the board to update
        pieces_list[start_row][start_col] = "x"  # Remove the piece from the starting position
        pieces_list[end_row][end_col] = current_piece  # Move the piece to the target position

        # Convert the board back to tuples
        self.pieces = tuple([tuple(row) for row in pieces_list])

        # Display the board after the move
        self.print_board()

    def convert_2d_array_indices_into_chess(self, algebraic_notation):
        row = algebraic_notation[1]  # Corrected to use the first element for row
        row = int(row)

        column = algebraic_notation[4]  # Corrected to use the second element for column
        column = int(column)  # Properly convert column to an integer

        # Convert the column (X-axis) back to a letter
        column_letter = chr(column + ord('a'))

        # Convert the row (Y-axis) back to a number (chessboard rows are from 1 to 8)
        row_number = 8 - row

        return f"{column_letter}{row_number}"
