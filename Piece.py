class Piece:

    def __init__(self, piece_type="piece", x=0, y=0, is_big=False, piece_type_letter=' '):
        self.type = piece_type
        self.x = x
        self.y = y
        self.is_big = is_big
        self.piece_type_letter = piece_type_letter
    def __str__(self):
        return self.piece_type_letter