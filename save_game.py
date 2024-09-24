__author__ = 'Luciano Cequinel'
__contact__ = 'lucianocequinel@gmail.com'
__version__ = '3.0.0'
__release_date__ = 'September, 25 2024'
__license__ = 'MIT'


import os
import nuke
from shutil import copyfile
from datetime import datetime


class SaveGame:
    def __init__(self):
        self.script_file = None
        self.original_path = None
        self.script_path = None

    def validate_script(self):
        if nuke.Root().name() != 'Root' :
            _force_save = nuke.scriptSave()
            self.script_path = nuke.Root().name()
            self.original_path, self.script_file = os.path.split(self.script_path)

            return True
        else:
            nuke.message('Must save or open a script first!')
            return False

    def create_destination_folder(self, sub_folder='save_game'):
        save_path = '/'.join([self.original_path, sub_folder])

        if not os.path.isdir(save_path):
            os.mkdir(save_path)
            print('\t>> Created save game folder {}'.format(save_path))

        return save_path

    def create_destination_path(self, sub_folder='save_game'):
        now = datetime.now().strftime("%b_%d_%H_%M_%S")

        save_path = '/'.join([self.original_path, sub_folder])

        if not os.path.isdir(save_path):
            os.mkdir(save_path)
            nuke.warning('\t>> Created save game folder')
            nuke.warning('\t>> {}'.format(save_path))

        destination_filename = self.script_file.replace('.nk', '_{}.nk'.format(now))
        destination_path = '/'.join([save_path, destination_filename])

        return destination_path

    def save_game(self, sub_folder='save_game'):
        if self.validate_script():
            nuke.warning('')
            nuke.warning(''.rjust(60, '*'))
            nuke.warning('\t >> Saving game'.center(60, '.'))

            destination_path = self.create_destination_path(sub_folder=sub_folder)

            copyfile(self.script_path, destination_path)

            nuke.warning('\t>> {} saved correctly!'.format(destination_path))
            nuke.warning(''.rjust(60, '*'))
            nuke.warning('')
            return destination_path

        return False

if __name__ == '__main__':
    save = SaveGame().save_game()
