#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import fileinput
import re
import sys

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    rank = []
    for line in fileinput.input(files=filename):
        search = re.search(r'.*Popularity in (\d{4}).*', line)

        if search:
            year = search.group(1)
            rank.append(year)

        search = re.search(r'<tr align="right"><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td>', line)

        if search:
            pos = search.group(1)
            male = search.group(2)
            female = search.group(3)

            rank.append("%s %s" % (male, pos))
            rank.append("%s %s" % (female, pos))        

    rank.sort()

    return rank

def print_summary(rank):
    text = '\n'.join(rank[:10]) + '\n...'
    print(text)

    return

def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

        # For each filename, get the names, then either print the text output
        # or write it to a summary file
    
    for file in args:
        rank = extract_names(file)

        if summary:
            print_summary(rank)


if __name__ == '__main__':
    main()
