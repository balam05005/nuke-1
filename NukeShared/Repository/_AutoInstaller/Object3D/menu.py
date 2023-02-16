#############################################################
###################3D OBJECT v1.3############################
##############compatible with Nuke 13########################
#################by Andrea Geremia###########################
###############www.andreageremia.it##########################
#############################################################

import sys
import nuke
import os

#*****************************************************************
#*****************************************************************
#******************ADD THIS TO YOUR FILE INIT.PY******************
#*************change 'yourPath' with the right name***************
#***************DON'T DELETE THE r BEFORE THE PATH****************
#nuke.pluginAddPath(r"/Users/yourPath/.nuke/3D_Object")
#*****************************************************************
#*****************************************************************


#Read Object3D folder path
Object3D_path = os.path.dirname(__file__)
print ("Object 3D path: " + Object3D_path)



toolbar = nuke.toolbar("Nodes")
m = toolbar.addMenu("3D Object v1.1", icon = os.path.join(Object3D_path, "icon/3D_Object.png"))



#BASIC OBJECTS low
m.addCommand('Basic Geometry/Low Res/cube', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "Basic/low/cube_low.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/cube.png"))   # in Windows I need to convert \ to / with --> replace('\\', '/')
m.addCommand('Basic Geometry/Low Res/cylinder', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "Basic/low/cylinder_low.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/cylinder.png"))
m.addCommand('Basic Geometry/Low Res/cone', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "Basic/low/cone_low.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/cone.png"))
m.addCommand('Basic Geometry/Low Res/pype', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "Basic/low/pype_low.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/pype.png"))
m.addCommand('Basic Geometry/Low Res/torus', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "Basic/low/torus_low.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/torus.png"))
m.addCommand('Basic Geometry/Low Res/pyramid 3sides', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "Basic/low/pyramid_3sides_low.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/pyramid.png"))
m.addCommand('Basic Geometry/Low Res/pyramid 4sides', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "Basic/low/pyramid_4sides_low.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/pyramid.png"))
m.addCommand('Basic Geometry/Low Res/pyramid 5sides', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "Basic/low/pyramid_5sides_low.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/pyramid.png"))



#BASIC OBJECTS high
m.addCommand('Basic Geometry/High Res/cube', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "Basic/high/cube.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/cube.png"))
m.addCommand('Basic Geometry/High Res/cylinder', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "Basic/high/cylinder.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/cylinder.png"))
m.addCommand('Basic Geometry/High Res/cone', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "Basic/high/cone.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/cone.png"))
m.addCommand('Basic Geometry/High Res/pype', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "Basic/high/pype.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/pype.png"))
m.addCommand('Basic Geometry/High Res/torus', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "Basic/high/torus.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/torus.png"))
m.addCommand('Basic Geometry/High Res/pyramid 3sides', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "Basic/high/pyramid_3sides.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/pyramid.png"))
m.addCommand('Basic Geometry/High Res/pyramid 4sides', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "Basic/high/pyramid_4sides.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/pyramid.png"))
m.addCommand('Basic Geometry/High Res/pyramid 5sides', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "Basic/high/pyramid_5sides.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/pyramid.png"))



#TEST GEOMETRY
m.addCommand('Test Geometry/buddha', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "TestGeometry/buddha.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/buddha.png"))
#m.addCommand('Test Geometry/buddha_low', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/TestGeometry/buddha_low.nk") + "\")", icon=os.path.join(Object3D_path, "icon/buddha.png"))

m.addCommand('Test Geometry/dragon', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "TestGeometry/dragon.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/dragon.png"))
#m.addCommand('Test Geometry/dragon_low', "nuke.nodePaste(\"" + os.path.join(Object3D_path + "/TestGeometry/dragon_low.nk") + "\")", icon=os.path.join(Object3D_path, "icon/dragon.png"))

m.addCommand('Test Geometry/human head', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "TestGeometry/human_head.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/human_head.png"))

m.addCommand('Test Geometry/teapot', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "TestGeometry/teapot.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/teapot.png"))
m.addCommand('Test Geometry/teapot_low', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "TestGeometry/teapot_low.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/teapot.png"))

m.addCommand('Test Geometry/monkey', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "TestGeometry/monkey.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/monkey.png"))

m.addCommand('Test Geometry/pig head', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "TestGeometry/pig_head.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/pig_head.png"))

m.addCommand('Test Geometry/rubber toy', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "TestGeometry/rubber_toy.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/rubber_toy.png"))

m.addCommand('Test Geometry/shaderBall', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "TestGeometry/shaderBall.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/shaderBall.png"))

#DEEP SCENE
m.addCommand('Test Deep/deepScene', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "TestDeep/deepScene.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/deepScene.jpg"))

#AOV SCENE
m.addCommand('Test AOVs/RenderAOV', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "TestAOV/renderAOV.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/render.png"))
m.addCommand('Test AOVs/SceneAOV', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "TestAOV/sceneAOV.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/aov.png"))

#TEST IMAGES
m.addCommand('Test Images/Kodak Digital LAD', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "TestImages/kodak.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/kodak.jpg"))
m.addCommand('Test Images/Green Screen', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "TestImages/greenScreen.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/green_screen.jpg"))
m.addCommand('Test Images/Green Screen Hair', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "TestImages/greenScreen_hair.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/green_screen_hair.jpg"))
m.addCommand('Test Images/Blue Screen', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "TestImages/blueScreen.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/blue_screen.jpg"))
m.addCommand('Test Images/Blue Screen Hair', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "TestImages/blueScreen_hair.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/blue_screen_hair.jpg"))


#TOOLS
m.addCommand('Tool/Background 3D', "nuke.createNode(\"" + os.path.join(Object3D_path, "Tool/background3D").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/wireframe.png"))
m.addCommand('Tool/UV Render', "nuke.createNode(\"" + os.path.join(Object3D_path, "Tool/UVRender").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/UV_cube.png"))
m.addCommand('Tool/Card 360', "nuke.createNode(\"" + os.path.join(Object3D_path, "Tool/Card360").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/card360.png"))
m.addCommand('Tool/DeepThickness', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "Tool/DeepThickness.nk").replace('\\', '/') + "\")")
m.addCommand('Tool/Coordinates', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "Tool/coordinates.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/coordinates.jpg"))
m.addCommand('Tool/C4x4', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "Tool/C4x4.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/coordinates.jpg"))


#TEXTURE
m.addCommand('Texture/CheckerBoard UV', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "Texture/CheckerBoard_UV.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/UV_mapper.jpg"))
m.addCommand('Texture/UV Map', "nuke.createNode(\"" + os.path.join(Object3D_path, "Texture/UVMap").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/UVMap.png"))
m.addCommand('Texture/Coordinates img', "nuke.nodePaste(\"" + os.path.join(Object3D_path, "Texture/coordinates_img.nk").replace('\\', '/') + "\")", icon=os.path.join(Object3D_path, "icon/coordinates.jpg"))



m.addSeparator()


#INFO
m.addCommand('Info e Tutorial', "nuke.tcl('start', 'http://www.andreageremia.it/tutorial_3dobject.html')", icon = os.path.join(Object3D_path, "icon/question_mark.png"))
