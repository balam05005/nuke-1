''' Add this to your menu.py '''

import nuke
##GS Tools##

show_menu = False
organize = True


toolbar = nuke.menu("Nodes")

if show_menu == True:
    m = toolbar.addMenu("GS_Tools", icon="GS_Icon.png")
    m_Caustics = m.addMenu("Caustics",icon="Caustics_Icon.png")
    m_Caustics.addCommand("Caustics", "nuke.createNode(\"GS_Caustics\")", icon="Caustics_Icon.png")

if organize == True: #
    toolbar.addCommand("Draw/Caustics", "nuke.createNode(\"GS_Caustics\")", icon="Caustics_Icon.png")
