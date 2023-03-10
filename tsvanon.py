import argparse
import sys
import uuid

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

def generate_random_id():
    return uuid.uuid4().hex[:8].upper()

def anonymize_header_line(outfile, headers):
    outfile.write(headers[0])
    anonymized_ids = list()
    for a in range(0, len(headers) - 1):
        anonymized_id = generate_random_id()
        anonymized_ids.append(anonymized_id)
        outfile.write('\t')
        outfile.write(anonymized_id)
    outfile.write('\n')
    def id_generator (input_list):
        for element in input_list:
            yield element
    return id_generator(anonymized_ids)

def anonymize_data_line(outfile, line, id=None):
    if id:
        outfile.write(id)
    else:
        outfile.write(generate_random_id())
    outfile.write(line[line.index('\t'):])

parser = argparse.ArgumentParser(
    prog = 'tsvanon',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description = description)
parser.add_argument('-m', '--method', required=True, choices=['rows', 'cols', 'both', 'keep'])
parser.add_argument('-i', '--infile', required=True, help='Filename or path for input file')
parser.add_argument('-o', '--outfile', required=True, help='Filename or path for output file')
args = parser.parse_args()

if args.infile == args.outfile:
    sys.exit("Input and output cannot be the same file.")

with open(args.infile, 'r') as infile, open(args.outfile, 'w') as outfile:
    if args.method == 'rows':
        outfile.write(next(infile))
        for line in infile:
            anonymize_data_line(outfile, line)
    elif args.method == 'cols':
        headers = next(infile).split('\t')
        anonymize_header_line(outfile, headers)
        for line in infile:
            outfile.write(line)
    elif args.method == 'both':
        headers = next(infile).split('\t')
        anonymize_header_line(outfile, headers)
        for line in infile:
            anonymize_data_line(outfile, line)
    elif args.method == 'keep':
        headers = next(infile).split('\t')
        anonymized_ids = anonymize_header_line(outfile, headers)
        for line in infile:
            anonymize_data_line(outfile, line, id=next(anonymized_ids))