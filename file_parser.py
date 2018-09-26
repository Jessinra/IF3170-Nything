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
            order_detail = FileParser.construct_order_details(line)
            parsed_data.append(order_detail)

        return parsed_data

    @staticmethod
    def construct_order_details(line):
        color, chess_type, count = line.strip().lower().split()
        order_detail = {
            'color': 'w' if color == 'white' else 'b',
            'type': chess_type,
            'count': int(count)
        }
        return order_detail
