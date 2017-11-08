
"""Usage:
go.py SHORTCUT
go.py (-h | --help)
go.py --version

Arguments:
    SHORTCUT    Shortcut of the place to open

Options:
    -h --help    Show this screen.
    -v --version    Show version.
"""
# go: program to open file explorers in pre-defined shortcut locations
# pdlfuente 2016-02-22
#
# se le pasa como argumento el shortcut que se haya definido y te abre el explorador de windows en la ubicacion correspondiente

#docopt help string

from docopt import docopt
import subprocess
import sys
import json

# code from Dietrich Epp answer in http://stackoverflow.com/questions/6631299/python-opening-a-folder-in-explorer-nautilus-mac-thingie
if sys.platform == 'darwin':
    def openFolder(path):
        subprocess.check_call(['open', '--', path])
elif sys.platform == 'linux2':
    def openFolder(path):
        subprocess.check_call(['xdg-open', '--', path])
elif sys.platform == 'win32':
    def openFolder(path):
        try:
            subprocess.check_call(['explorer', path])
        except:
            pass
# end of Drietrich Epp code

shortcut_dict={'s': 'C:\safety\enc\safEnc'}
        
        
        
if __name__ == '__main__':
    arguments = docopt(__doc__, version='go 0.1')
    shortcut = arguments['SHORTCUT']
    if shortcut:
        #with open('shortcut_list.txt', 'w') as f:
        #    json.dump(shortcut_dict, f)
        #    f.flush()
        #    f.close()
        
        
        #load shortcut dict from shortcut_list.txt file
        with open('shortcut_list.txt', 'r') as f:
            shortcut_dict = json.load(f)
            f.close()
        #    print shortcut_dict
        
        if shortcut in shortcut_dict:
           openFolder(shortcut_dict[shortcut])




