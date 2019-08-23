## -------------------------------------------------------------------------------------
# menu.py
# Version: 1.0.0 (Major,Minor,Revision)
# Last Updated: August 22nd, 2019
## -------------------------------------------------------------------------------------


## Importing modules -------------------------------------------------------------------
import nuke
import platform


## .nuke directory ---------------------------------------------------------------------
Win_Dir = 'P:\GDL\production\library\script\nuke'
Linux_Dir = '/home/user/.nuke'


#  Set global directory (Automatically detect OS system)
if platform.system() == "Windows":
	dir = Win_Dir
elif platform.system() == "Linux":
	dir = Linux_Dir
else:
	dir = none




## Default Nuke per show plugin path ---------------------------------------------------






## Cryptomatte -------------------------------------------------------------------------
#
#  Copyright (c) 2014, 2015, 2016, 2017 Psyop Media Company, LLC
#  See license.txt
#

import cryptomatte_utilities
cryptomatte_utilities.setup_cryptomatte_ui()



## Xtools ------------------------------------------------------------------------------

toolbar = nuke.toolbar("Nodes")
m = toolbar.addMenu("X_Tools", icon="X_Tools.png")

m.addCommand("X_Distort", "nuke.createNode(\"X_Distort\")", icon="X_Distort.png")
m.addCommand("X_Aton", "nuke.createNode(\"X_Aton\")", icon="X_Aton.png")
m.addCommand("X_Tesla", "nuke.createNode(\"X_Tesla\")", icon="X_Tesla.png")

