__author__ = 'josh'
import sys
import argparse
from urllib import urlencode
from urllib import FancyURLopener
from subprocess import Popen, PIPE

sys_args = sys.argv[1:]
parser = argparse.ArgumentParser()

# Default should be the result of the input file parsing of input file extension. TODO
parser.add_argument('-s', '--syntax', nargs='?', default='python', const='', metavar='Syntax',
                    help='Syntax highlighting for paste')
parser.add_argument('-u', '--user', '-p', '--poster', nargs='?', default='josh', const='DEFAULT_POSTER'
                    , metavar='Poster', help='Author of post')
parser.add_argument('infile', type=argparse.FileType('r'))

args = parser.parse_args(sys_args)

url_opener = FancyURLopener()
content = args.infile.read()
poster = args.user
syntax = args.syntax
if len(content) < 5:
    sys.exit('Trying to upload empty or nearly empty file.')
params = {'content': content, 'poster': poster}
if syntax:
    params['syntax'] = syntax
page = url_opener.open('http://paste.ubuntu.com', urlencode(params))
link = page.url

def to_clipboard(text):
    Popen(['xclip', '-selection', 'c'], stdin=PIPE).communicate(input=bytes(text))

# Adds link to clipboard using xclip on linux. If no xclip, will break.
to_clipboard(link)
print('Copied to clipboard: ' + link)
