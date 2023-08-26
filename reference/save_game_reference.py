import re
from datetime import datetime
from os import mkdir, path
from shutil import copyfile

import nuke


"""

choice = nuke.choice('Opening history', 'open as', ['version up', 'untitled'], 1)
print(choice)
"""

def get_version_from_file(filename):
    version = '001'
    regex = 'v[0-9]{3}'
    match = re.findall(regex, filename, re.IGNORECASE)[0]
    version = match.replace('v', '')
    return(version)

def create_directory(dirname):
    if path.isdir(dirname):
        pass
        #print('history folder already exists')
    else:
        mkdir(dirname)
        print('created history folder')
    return()

def save_game(script):
    dirname, filename = path.dirname(script), path.basename(script)

    historyFolder = '/'.join([dirname, 'history'])
    create_dir = create_directory(historyFolder)

    _date = datetime.now().strftime("%b%d_%H_%M")

    save_name =  filename.replace('.nk', '.{}.nk'.format(_date))

    saveFilename = '/'.join([historyFolder, save_name])
    print('Nuke Script saved to history folder!\n', saveFilename) 

    _copy = copyfile(script, saveFilename)

    return()

def run():
    script = nuke.Root()['name'].value()

    if nuke.Root().name() == 'Root':
        nuke.message('Must save or open a script first!')
        return()
    else:
        forceSave = nuke.scriptSave()
        save = save_game(script)

    return()



#def load_backup():
#   if 'history' in nuke.Root().name():
#        result = nuke.ask('Opening a script from history folder\nDo you want to save it in the correct path?')
#        if result:
#            print('testing if OK')
#        else:
#            print('canceled by user')

#add = nuke.addOnScriptLoad(load_backup)
        

#menu = nuke.menu('Nuke').addMenu('save game')
#menu.addCommand('save game', 'run()')


if __name__ == '__main__':
    run()
