#!/usr/bin/env python
import argparse
import re

parser = argparse.ArgumentParser(description='Convert from Markdown file to CSV')
parser.add_argument('file', type=str, help='the .MD file')
parser.add_argument('--delimiter', default=",",
                   help='delimiter character')

args = parser.parse_args()
md_path = args.file
delimiter = args.delimiter
hasHeader = False

with open(md_path, 'rU') as f_obj:
  mdContent = f_obj.read()
columns = mdContent.split('\n')
for i, e in enumerate(columns):
  if i == 1:
    if not any(c.isalpha() for c in e):
      hasHeader = True
    continue
  x = re.sub(r'^\|\s*?(\S)', r'\1', e)
  x = re.sub(r'(\S)\s*?\|', r'\1|', x)
  x = re.sub(r'\|\s*?(\S)', delimiter+r'\1', x)
  x = re.sub(r'(\S)\s*?\|$', r'\1', x)

  print x

