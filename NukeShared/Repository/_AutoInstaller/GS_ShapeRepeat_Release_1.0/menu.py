''' Add this to your menu.py '''

import nuke
##GS Tools##
show_menu = False
organize = True

toolbar = nuke.menu("Nodes")

if show_menu == True:
    m = toolbar.addMenu("GS_Tools", icon="GS_Icon.png")
    m_ShapeRepeat = m.addMenu("ShapeRepeat",icon="ShapeRepeat_Icon.png")

    m_ShapeRepeat.addCommand("ShapeRepeat", "nuke.createNode(\"GS_ShapeRepeat\")", icon="ShapeRepeat_Icon.png")

if organize == True: #
    toolbar.addCommand("Draw/ShapeRepeat", "nuke.createNode(\"GS_ShapeRepeat\")", icon="ShapeRepeat_Icon.png")