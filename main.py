# yet to program:
# piece promotion
# castling
# en passant

alphabet_converter = {1: 'a', 2: 'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h'}
colors = ['White', 'Black']

class Place:
    """A single square on the board."""
    is_back_rank = False
    next_id = 1

    def __init__(self, color, coordinates):
        self.color = color
        self.piece = None
        self.coordinates = coordinates
        self.location = str(alphabet_converter[self.coordinates[0]]) + str(self.coordinates[1])

    def add_piece(self, piece):
        self.piece = piece

    def remove_piece(self):
        self.piece = None


class BackRank(Place):
    """The opponent's back rank."""
    is_back_rank = True

    def __init__(self, color):
        super().__init__(color)

    def add_piece(self, piece):
        if piece is type(Pawn):
            self.piece = Queen #Autoqueens, need to figure out promotion otherwise
        else:
            self.piece = piece



class Piece():
    """Pieces that play the game."""

    def __init__(self, color, place):
        self.color = color
        self.place = place
        self.location = self.place.location
    
    def move(self, start, end):
        start.remove_piece(self)
        if end.piece:
            end.remove_piece(end.piece)
        end.add_piece(self)


class King(Piece):
    """The King"""


class Queen(Piece):
    """The Queen"""


class Rook(Piece):
    """The Rook"""


class Bishop(Piece):
    """The Bishop"""


class Knight(Piece):
    """The Knight"""


class Pawn(Piece):
    """The Pawn"""


class GameState:
    """A collective that manages the global game state."""

    def __init__(self, places, pieces, turn, dimensions=(8,8)):
        self.places = {place: place.piece for place in places if place.piece != None}
        self.pieces = {which_color: piece for piece in pieces if piece.color == which_color for which_color in colors}
        self.turn = turn
        self.dimensions = dimensions

    def end_game(self):
        for i in range(2):
            if King not in self.pieces[i]:
                raise GameOver()
            
    def register_place(place):
        pass


class GameOver():
    """Ends the game."""
    pass

def layout(width, length):
    for i in range(width):
        for j in range(length):
            pass