class FileParser:
    @staticmethod
    def read_file(filename=None):
        f = open(filename, 'r', encoding="utf-8")
        return f.readlines()

    @staticmethod
    def parse_data(filename=None):
        raw_creation_list = FileParser.read_file(filename)

        parsed_data = []
        for line in raw_creation_list:
            parsed_line = FileParser.parse_line(line)
            parsed_data.append(parsed_line)

        return parsed_data

    @staticmethod
    def parse_line(text_line):
        color, chess_type, count = text_line.strip().lower().split()
        parsed_line = {
            'color': 'w' if color == 'white' else 'b',
            'type': chess_type,
            'count': int(count)
        }
        return parsed_line