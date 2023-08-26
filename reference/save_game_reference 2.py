import nukescripts
from shutil import copy2
from shutil import copyfile
from shutil import copyfileobj
import os
from datetime import datetime

def copyScript():

    print
    nuke.scriptSave() #force save

    scriptFile = nuke.scriptName()
    scriptName = scriptFile.split('/')[-1]

    now = datetime.now()
    now = now.strftime("%b_%d-%H_%M_%S")

    bkpFile = scriptName.replace('.nk', '_%s.nk' %(now))

    scriptFolder = nuke.script_directory()

    newFolder = ('/backup/')
    bkpFolder = (scriptFolder + newFolder)

    print 'script file: ' + scriptFile
    print 'script name: ' + scriptName
    print 'bkp name: ' + bkpFile
    print
    print 'script folder: ' + scriptFolder
    print 'bkpFolder: ' + bkpFolder

    print

    try:
        os.mkdir(bkpFolder)
        print ('Created backup folder: ' + bkpFolder)
    except:
        print ('Backup folder already exist! %s' %(bkpFolder))

    origin = scriptFolder + '/'
    destination = bkpFolder + bkpFile

    print
    print origin
    print
    print destination

    #copy2(origin, destination)
    #copyfile(origin, destination)


    #filename1 = r'C:\Users\DelftStack\Documents\test\test.txt'
    originRB = open(origin, 'rb')
    #destination = r'C:\Users\DelftStack\Pictures\test2\test2.txt'
    destinationWB = open(destination, 'wb')

    shutil.copyfileobj(originRB, destinationWB)







copyScript()



