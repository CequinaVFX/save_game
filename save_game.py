
__author__ = 'Luciano Cequinel'
__contact__ = 'lucianocequinel@gmail.com'
__version__ = '2.0.4'
__release_date__ = 'November, 04 2023'
__license__ = 'MIT'


import os
import nuke
from shutil import copyfile
from datetime import datetime


class SaveGame:
    def validate_script(self):
        if nuke.Root().name() != 'Root' :
            _force_save = nuke.scriptSave()
            self.script_path = nuke.Root().name()
            self.original_path, self.script_file = os.path.split(self.script_path)

            return True
        else:
            nuke.message('\t>> Must save or open a script first!')
            return False

    def create_destination_folder(self):
        save_path = '/'.join([self.original_path, 'save_game'])

        if not os.path.isdir(save_path):
            os.mkdir(save_path)
            print('\t>> Created save game folder {}'.format(save_path))

        return save_path

    def create_destination_path(self):
        now = datetime.now().strftime("%b_%d_%H_%M_%S")

        save_path = self.create_destination_folder()
        destination_filename = self.script_file.replace('.nk', '_{}.nk'.format(now))
        destination_path = '/'.join([save_path, destination_filename])

        return destination_path

    def save_game(self):
        if self.validate_script():
            nuke.warning(''.rjust(60, '*'))
            nuke.warning(' Saving game'.center(60, '.'))

            destination_path = self.create_destination_path()

            copyfile(self.script_path, destination_path)

            nuke.warning(' >> {} saved correctly!'.format(destination_path))
            nuke.warning(''.rjust(60, '*'))
            return True

        return False

if __name__ == '__main__':
    save = SaveGame().save_game()
    print('Game saved to {}'.format(save))
