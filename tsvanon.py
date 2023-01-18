import argparse

description = """
tsvanon.py - Anonymize ids in tsv files

methods:
- rows: anonymize first column of all rows (except the first row)
- cols: anonymize all columns of first row (except the first column)
- both: anonymize both of the above
- keep: anonymize both columns and rows, keep matching pairs

With the keep method, any id in the rows that is identical with an id in the columns
(or vice versa) will be replaced with identical values in both row and column.
"""

parser = argparse.ArgumentParser(
    prog = 'tsvanon',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description = description)
parser.add_argument('-m', '--method', required=True, choices=['rows', 'cols', 'both', 'keep'])
parser.add_argument('-i', '--infile', required=True, help='Filename or path for input file')
parser.add_argument('-o', '--outfile', required=True, help='Filename or path for output file')
args = parser.parse_args()

