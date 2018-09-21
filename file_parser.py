from chess_piece.factory import ChessPieceFactory

class FileParser:
    @staticmethod
    def read_file(filename=None):
        f = open(filename, 'r', encoding="utf-8")
        return f.readlines()

    @staticmethod
    def parse_data(filename=None):
        raw_data = FileParser.read_file(filename)
        parsed_data = []

        for row in raw_data:
            split_row = row.strip().lower().split()
            color, chess_type, count = split_row
            color = 'w' if color == 'white' else 'b'
            count = int(count)
            parsed_data.append({
                'color': color,
                'type': chess_type,
                'count': count
            })

        return parsed_data

    @classmethod
    def load(cls, board, filename):
        board.initialize_board()
        data = cls.parse_data(filename)
        for d in data:
            for _ in range(d['count']):
                chess_piece = ChessPieceFactory.create_chess_piece(d['type'], d['color'])
                board.add_piece_randomly(chess_piece)

        return board