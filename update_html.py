#!/usr/bin/python3
import argparse
import os

parser = argparse.ArgumentParser(description='Updates html files to have same assets and navbar as in "template.html", \
                                              \nThe updating is done according to "PAGE CONTENT" comments in the html files.')
parser.add_argument('inputs', type=str, nargs='+')
parser.add_argument('--mode', type=str,
                    help='set input mode, default: filenames, "dir": directories, "recursive": not implemented yet.')

args = parser.parse_args()

mode = args.mode if args.mode else "filename"

splitter = 'PAGE CONTENT'

with open('template.html', 'r') as template_file:
    template_html = template_file.read()

template_parts = template_html.split(splitter)
template_begin = template_parts[0]
template_end = template_parts[-1]

def update_to_match_template(filename):
    with open(filename, 'r') as html_file:
        html = html_file.read()

    html_content = html.split(splitter)[1]
    updated_html_parts = (template_begin, html_content, template_end)

    with open(filename, 'w') as html_file:
        html_file.write(splitter.join(updated_html_parts))
        print('updated file', filename)

if mode == "filename":
    for filename in args.inputs:
        update_to_match_template(filename)

if mode == "dir":
    for directory in args.inputs:
        print('updating files in directory {}...'.format(directory))
        for filename in [fn for fn in os.listdir(directory) if len(fn) > 5 and fn[-5:] == '.html']:
            update_to_match_template(os.path.join(directory, filename))
