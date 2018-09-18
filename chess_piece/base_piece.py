class ChessPiece:
    def __init__(self, color):
        self.position = (None, None)    # For GA purpose
        self.color = color

    def move(self, position):
        self.position = position
    
    def get_attack_pattern(self):
        raise NotImplementedError("Get_attack_pattern method is not implemented yet !")