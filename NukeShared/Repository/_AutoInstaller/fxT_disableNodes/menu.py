# add fxT menu
sideBar = nuke.menu('Nodes')

#fxT = sideBar.addMenu('Tools/fxT', icon='fxT_menu.png')

# add fxT_disableNodes Gizmo to the fxT menu
sideBar.addCommand('Tools/fxT_disableNodes', "nuke.createNode('fxT_disableNodes')", 'Alt+d', icon='fxT_disableNodes.png')