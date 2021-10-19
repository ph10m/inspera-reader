import argparse
import textwrap
from inspera import InsperaReader

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