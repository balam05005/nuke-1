''' Add this to your menu.py '''
import nuke
##GS Tools##

show_menu = False
organize = True


toolbar = nuke.menu("Nodes")

if show_menu == True:
    m = toolbar.addMenu("GS_Tools", icon="GS_Icon.png")
    m_FireSparks = m.addMenu("FireSparks",icon="Fire_Icon.png")

    m_FireSparks.addCommand("Particle", "nuke.createNode(\"GS_Particle\")", icon="Particle_Icon.png")
    m_FireSparks.addCommand("Sparks", "nuke.createNode(\"GS_Sparks\")", icon="Sparks_Icon.png")
    m_FireSparks.addCommand("Fire", "nuke.createNode(\"GS_Fire\")", icon="Fire_Icon.png")

if organize == True: #
    toolbar.addCommand("Particles/Particle", "nuke.createNode(\"GS_Particle\")", icon="Particle_Icon.png")
    toolbar.addCommand("Particles/Sparks", "nuke.createNode(\"GS_Sparks\")", icon="Sparks_Icon.png")
    toolbar.addCommand("Particles/Fire", "nuke.createNode(\"GS_Fire\")", icon="Fire_Icon.png")
