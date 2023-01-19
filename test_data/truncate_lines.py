with open('long_lines.tsv', 'r') as infile, open ('short_lines.tsv', 'w') as outfile:
    for long_line in infile:
        items = long_line.split('\t')
        few_items = items[:11]
        outfile.write('\t'.join(few_items))
        outfile.write('\n')