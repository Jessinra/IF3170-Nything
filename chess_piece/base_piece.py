class ChessPiece:
    def __init__(self, color):
        self.position = (None, None)  # For GA purpose
        self.color = color

    @staticmethod
    def get_default_attack_pattern():
        return {
            "N": [],
            "E": [],
            "S": [],
            "W": [],
            "NE": [],
            "NW": [],
            "SW": [],
            "SE": []
        }

    def __str__(self):
        char = self.__class__.__name__[0]
        if self.color == 'w':
            char = char.upper()
        return char

    def move(self, position):
        self.position = position

    def get_attack_pattern(self):
        raise NotImplementedError("Get_attack_pattern method is not implemented yet !")
