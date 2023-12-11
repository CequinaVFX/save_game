import nuke
import save_game

SHORTCUT = 'ctrl+alt+shift+s'
ICON = 'save_game.png'

#Add a menu and assign a shortcut
toolbar = nuke.menu('Nodes')
customTools = toolbar.addMenu('CQN Tools', icon='Modify.png')
customTools.addCommand('Save game', 'save_game.SaveGame().save_game()', SHORTCUT, icon=ICON)
