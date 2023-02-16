''' Add this to your menu.py '''

import nuke
##GS Tools##
show_menu = False
organize = True


toolbar = nuke.menu("Nodes")

if show_menu == True:
    m = toolbar.addMenu("GS_Tools", icon="GS_Icon.png")
    m_Edge_Extend = m.addMenu("Edge_Extend",icon="GS_Icon_Edge_Extend.png")

    m_Edge_Extend.addCommand("Edge_Extend", "nuke.createNode(\"GS_Edge_Extend\")", icon="GS_Icon_Edge_Extend.png")

if organize == True:
    toolbar.addCommand("Draw/EDGE EXTENDS/Edge_Extend", "nuke.createNode(\"GS_Edge_Extend\")", icon="GS_Icon_Edge_Extend.png")
