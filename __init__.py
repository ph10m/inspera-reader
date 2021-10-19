import argparse
import textwrap
import json
from .inspera.candidate import InsperaCandidate

class InsperaReader:
    def __init__(self, file):
        self.json_data = None
        self.parsed_json = {}
        with open(file, 'r', encoding='utf8') as f:
            self.json_data = json.load(f)

    def candidates(self):
        raw = self.json_data['ext_inspera_candidates']
        return [InsperaCandidate(c['result']) for c in raw]

    def __str__(self):
        return 'Inspera data for the course: {}'.format(self.json_data['ext_inspera_assessmentRunTitle'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='InsperaReader',
        epilog=textwrap.dedent('''\
            Info:
            - For each candidate given in the source data, a data field of each response is made, with the following fields:
                - question id -> int
                - response (raw) -> str
                - response (parsed) -> str
                - grading -> list[int]
                - max_score -> int
                - duration -> int
            ''')
    )

    file_help = 'The path for the .json file from Inspera'
    parser.add_argument('-f', '--file', required=True, type=str, help=file_help)

    args = parser.parse_args()
    reader = InsperaReader(args.file)
