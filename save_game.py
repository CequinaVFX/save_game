#******************************************************
# content: 
#
# version: 1.0.0
# date: August 26 2023
#
# how to: ()
# dependencies: nuke, os.path, datetime.datetime
#
# license: MIT
# author: Luciano Cequinel [lucianocequinel@gmail.com]
#******************************************************

import nuke
from os import path
from datetime import datetime
from os import mkdir, path
from shutil import copyfile
print()
class SaveGame():
    def __init__(self):
        forceSave = nuke.scriptSave()
        self.scriptPath = (nuke.Root().name())
        self.dirPath, self.scriptName = path.split(self.scriptPath)

    def save_game(self):
        self.backupName = self._edit_filename(self.scriptName)
        self.save_DirPath = self._saveDirPath()
        copy = self.copy_file()
        return(self.backupName, self.save_DirPath, copy)

    def _saveDirPath(self):
        savePath = '/'.join([self.dirPath, 'save_game'])
        if not path.isdir(savePath):
            mkdir(savePath)
            print('created history folder {}'.format(savePath))
        return(savePath)

    def _edit_filename(self, scriptName):
        now = datetime.now().strftime("%b_%d_%H_%M_%S")
        return(scriptName.replace('.nk', '_{}.nk'.format(now)))

    def copy_file(self):
        _finalPath = '/'.join([self.save_DirPath, self.backupName])
        print('copy... ', self.scriptPath, _finalPath)
        copy = copyfile(self.scriptPath, _finalPath)
        return(_finalPath)

def save_game():
    if nuke.Root().name() == 'Root':
        nuke.message('Must save or open a script first!')
        return()
    else:
        save = SaveGame().save_game()
        return(save)
        

if __name__ == '__main__':
    save = save_game()