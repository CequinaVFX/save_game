import nuke
import save_game

SHORTCUT = 'ctrl + alt + shift + s'

#Add a menu and assign a shortcut
toolbar = nuke.menu('Nodes')
cqnTools = toolbar.addMenu('CQNTools', icon='Modify.png')
cqnTools.addCommand('Save game', 'save_game.save_game()', SHORTCUT, icon='Sparkles.png')