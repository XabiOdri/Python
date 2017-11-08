
"""Usage:
run.py SHORTCUT [OTHER_ARGUMENTS...]
run.py (-h | --help)
run.py --version

Arguments:
    SHORTCUT            Shortcut of the app to run
    OTHER_ARGUMENTS       additional arguments

Options:
    -h --help    Show this screen.
    -v --version    Show version.
"""
# run: program to run applications with arguments with predefined shortcuts
# pdlfuente 2016-03-14
#
# se le pasa como argumento el shortcut que se haya definido y te abre la aplicacion correspondiente con los argumentos correspondientes

from docopt import docopt
import subprocess
import sys
import json

def run(shortcut, other_arguments):
    items = shortcut.split()
    shortcut_list = []
    for i in items:
        shortcut_list.append(i.encode('utf-8'))
    for i in other_arguments:
        shortcut_list.append(i.encode('utf-8'))
    subprocess.Popen(shortcut_list)


if __name__ == '__main__':
    arguments = docopt(__doc__, version='go 0.1')
    shortcut = arguments['SHORTCUT']
    other_arguments = arguments['OTHER_ARGUMENTS']
    if shortcut:
        #load shortcut dict from shortcut_list.txt file
        with open('shortcut_list.txt', 'r') as f:
            shortcut_dict = json.load(f)
            f.close()
        #    print shortcut_dict
        if shortcut in shortcut_dict:
           run(shortcut_dict[shortcut], other_arguments)




