##************************************************************************************##
## -------------------------------------------------------------------------------------
# menu.py
# Version: 1.0.5 (Major,Minor,Revision)
#
# Last Modified by: Kalvin Irawan
# Last Updated: September 11th, 2019
## -------------------------------------------------------------------------------------
##************************************************************************************##




##************************************************************************************##
## -------------------------------------------------------------------------------------
##  GLOBAL IMPORTS :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
## -------------------------------------------------------------------------------------
##************************************************************************************##

## Global modules ----------------------------------------------------------------------
import nuke
import nukescripts
import platform

## In House modules --------------------------------------------------------------------
import lmnShuffle
import listNavigator
import filePathLister

## Third Party modules -----------------------------------------------------------------
##-----Cryptomatte ----Copyright (c) 2014, 2015, 2016, 2017 Psyop Media Company, LLC----
import cryptomatte_utilities
cryptomatte_utilities.setup_cryptomatte_ui()








## .nuke directory ---------------------------------------------------------------------
Win_Dir = 'P:/GDL/production/library/script/nuke'
Linux_Dir = '/home/user/.nuke'


## Set global directory (Automatically detect OS system) -------------------------------
if platform.system() == "Windows":
	dir = Win_Dir
elif platform.system() == "Linux":
	dir = Linux_Dir
else:
	dir = none

## Knob defaults -----------------------------------------------------------------------
nuke.knobDefault('Shuffle.label', "[value in]")

#cameras in real world are always centered
nuke.knobDefault('Card3D.shutteroffset',"centered")
nuke.knobDefault('TransformMasked.shutteroffset',"centered")
nuke.knobDefault('Transform.shutteroffset',"centered")
nuke.knobDefault('CameraShake3.shutteroffset',"centered")
nuke.knobDefault('CornerPin2D.shutteroffset',"centered")
nuke.knobDefault('Reconcile3D.shutteroffset',"centered")
nuke.knobDefault('Stabilize2D.shutteroffset',"centered")

nuke.knobDefault('Tracker4.shutteroffset', "centered") 
nuke.knobDefault('Tracker4.label', "Motion: [value transform]\nRef Frame: [value reference_frame]")
nuke.addOnUserCreate(lambda:nuke.thisNode()['reference_frame'].setValue(nuke.frame()), nodeClass='Tracker4')

nuke.addOnUserCreate(lambda:nuke.thisNode()['first_frame'].setValue(nuke.frame()), nodeClass='FrameHold')





##************************************************************************************##
## -------------------------------------------------------------------------------------
##  CUSTOM MENUS :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
## -------------------------------------------------------------------------------------
##************************************************************************************##

## Lumine Tab --------------------------------------------------------------------------

lt = nuke.menu('Nuke').addMenu('Lumine')


ltg = lt.addMenu('Gizmos')


lts = lt.addMenu('Scripts')
lts.addCommand('Autocrop', 'nukescripts.autocrop()')   ## this is nuke native


ltn = lt.addMenu('Nukepedia')
ltn.addCommand('expoglow', "nuke.createNode('expoglow')")
ltn.addCommand('aov_krakout', "nuke.createNode('aov_krakout')")
ltn.addCommand('Bloom', "nuke.createNode('Bloom')")
ltn.addCommand('Breakdown_Maker', "nuke.createNode('Breakdown_Maker')")
ltn.addCommand('Breakdown_Tool', "nuke.createNode('Breakdown_Tool')")
ltn.addCommand('HDRPrepper', "nuke.createNode('HDRPrepper')")


## Lumine Menu -------------------------------------------------------------------------

#lm = nuke.toolbar("Nodes").addMenu('lumine', icon="lmn_tools.png")

lm = nuke.menu('Nodes').addMenu('Lumine', icon="lmn_Tools_orange.png")


## HOP
H_lm = lm.addMenu("HOP", icon="hope_logo_white.png")
H_lm.addCommand("HOP_assets_reviewCard","nuke.createNode(\"HOP_assets_reviewCard\")", icon="hope_logo_AR_grey.png")
H_lm.addCommand("HOP_sequence_reviewCard","nuke.createNode(\"HOP_sequence_reviewCard\")", icon="hope_logo_SR_grey.png")

## bm_tools ----------------------------------------------------------------------------
B_lm = lm.addMenu("bm_Tools", icon="bm_Tools.png")
B_lm.addCommand("bm_CameraShake", "nuke.createNode(\"bm_CameraShake\")", icon="bm_CameraShake.png")
B_lm.addCommand("bm_CurveRemapper", "nuke.createNode(\"bm_CurveRemapper\")")
B_lm.addCommand("bm_EdgeMatte", "nuke.createNode(\"bm_EdgeMatte\")")
B_lm.addCommand("bm_GrainTransfer", "nuke.createNode(\"bm_GrainTransfer\")")
B_lm.addCommand("bm_Lightwrap", "nuke.createNode(\"bm_Lightwrap\")")
B_lm.addCommand("bm_MatteCheck", "nuke.createNode(\"bm_MatteCheck\")")
B_lm.addCommand("bm_NoiseGen", "nuke.createNode(\"bm_NoiseGen\")")
B_lm.addCommand("bm_Opticalmlow", "nuke.createNode(\"bm_Opticalmlow\")")
B_lm.addCommand("bm_StereoCheck", "nuke.createNode(\"bm_StereoCheck\")")


## Xtools ------------------------------------------------------------------------------
X_lm = lm.addMenu("X_Tools", icon="X_Tools.png")
X_lm.addCommand("X_Distort", "nuke.createNode(\"X_Distort\")", icon="X_Distort.png")
X_lm.addCommand("X_Aton", "nuke.createNode(\"X_Aton\")", icon="X_Aton.png")
X_lm.addCommand("X_Tesla", "nuke.createNode(\"X_Tesla\")", icon="X_Tesla.png")


## Menu add items ----------------------------------------------------------------------
mergeMenu = nuke.menu('Nodes').findItem("Merge/Merges")

mergeMenu.addCommand('Stencil', 'nuke.createNode("Merge2","operation stencil bbox B")', icon="MergeOut.png")
mergeMenu.addCommand('Divide', 'nuke.createNode("Merge2", "operation divide")', icon="In.png")
mergeMenu.addCommand('Mask', 'nuke.createNode("Merge2", "operation mask bbox A")', icon="In.png")

filterMenu = nuke.menu('Nodes').findItem("Filter")
filterMenu.addCommand('Blocky',"nuke.createNode('Blocky')")

