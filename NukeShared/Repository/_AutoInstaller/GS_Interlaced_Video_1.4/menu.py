''' Add this to your menu.py '''

import nuke
##GS Tools##

show_menu = False
organize = True

toolbar = nuke.menu("Nodes")

if show_menu == True:
    m = toolbar.addMenu("GS_Tools", icon="GS_Icon.png")
    m_Interlaced_video = m.addMenu("Interlaced_video",icon="Interlaced_Icon.png")

    m_Interlaced_video.addCommand("Interlaced_video", "nuke.createNode(\"GS_Interlaced_video\")", icon="Interlaced_Icon.png")

if organize == True: #
    toolbar.addCommand("Filter/Interlaced_video", "nuke.createNode(\"GS_Interlaced_video\")", icon="Interlaced_Icon.png")