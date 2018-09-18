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
            split_row = row.strip().split()
            parsed_data.append(split_row)

        return parsed_data
