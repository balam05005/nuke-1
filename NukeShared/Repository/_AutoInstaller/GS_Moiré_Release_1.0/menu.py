''' Add this to your menu.py '''

import nuke
##GS Tools##

show_menu = False
organize = True

toolbar = nuke.menu("Nodes")

if show_menu == True:
    m = toolbar.addMenu("GS_Tools", icon="GS_Icon.png")
    m_Moire = m.addMenu("Moire",icon="Moire_Icon.png")

    m_Moire.addCommand("Moire", "nuke.createNode(\"GS_Moire\")", icon="Moire_Icon.png")

if organize == True: #

    toolbar.addCommand("Filter/Moire", "nuke.createNode(\"GS_Moire\")", icon="Moire_Icon.png")