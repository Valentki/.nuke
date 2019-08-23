## -------------------------------------------------------------------------------------
# init.py
# Version: 1.0.0 (Major,Minor,Revision)
# Last Updated: August 22nd, 2019
## -------------------------------------------------------------------------------------



## Per show plugin path ---------------------------------------------------
nuke.pluginAddPath('./gizmos')
nuke.pluginAddPath('./python')


## Cryptomatte -------------------------------------------------------------------------
#
#  Copyright (c) 2014, 2015, 2016, 2017 Psyop Media Company, LLC
#  See license.txt
#


nuke.pluginAddPath('./python/Cryptomatte')

import cryptomatte_utilities
cryptomatte_utilities.setup_cryptomatte()



## Xtools ------------------------------------------------------------------------------
nuke.pluginAddPath('./python/X_Tools')
nuke.pluginAddPath('./python/X_Tools/Icons')
nuke.pluginAddPath('./python/X_Tools/Gizmos')



## KeenTools ---------------------------------------------------------------------------
nuke.pluginAddPath('./python/KeenTools')


