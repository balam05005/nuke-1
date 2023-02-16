#*****************************************************************
#*****************************************************************
#*****************************************************************
#*****************EXPRESSION COLLECTION FOR NUKE******************
#******************v1.3 compatible with Nuke 13*******************
#*****************************************************************
#******************ADD THIS TO YOUR FILE INIT.PY******************
#***************DON'T DELETE THE r BEFORE THE PATH****************
#nuke.pluginAddPath(r"/Users/yourPath/.nuke/Expression")
#*****************************************************************
#*****************************************************************




import sys
import nuke
import os
import webbrowser


#Read Expression folder path
Expression_path = os.path.dirname(__file__)
print ("Expression path: " + Expression_path)


toolbar = nuke.toolbar("Nodes")
m = toolbar.addMenu("Expression Nodes", icon = os.path.join(Expression_path, "icon/expr.png"))

m.addMenu( 'Creations', icon = os.path.join(Expression_path, "icon/01.png") )
m.addMenu( 'Alpha', icon = os.path.join(Expression_path, "icon/02.png") )
m.addMenu( 'Pixel', icon = os.path.join(Expression_path, "icon/03.png") )
m.addMenu( 'Keying and Despill', icon = os.path.join(Expression_path, "icon/04.png") )
m.addMenu( 'Transform', icon = os.path.join(Expression_path, "icon/05.png") )
m.addMenu( '3D and Deep', icon = os.path.join(Expression_path, "icon/06.png") )



#CREATIONS
m.addCommand('Creations/Random/Random Colors', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Creations/Random/Random_colors.nk").replace('\\', '/') + "\")")     # in Windows I need to convert \ to / with --> replace('\\', '/'),
m.addCommand('Creations/Random/Random every Frame', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Creations/Random/Random_every_frame.nk").replace('\\', '/') + "\")")
m.addCommand('Creations/Random/Random every Pixel', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Creations/Random/Random_every_pixel.nk").replace('\\', '/') + "\")")
m.addCommand('Creations/Noise/Noise', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Creations/Noise/Noise.nk").replace('\\', '/') + "\")")
m.addCommand('Creations/Noise/fBm', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Creations/Noise/fBm.nk").replace('\\', '/') + "\")")
m.addCommand('Creations/Noise/Turbulence', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Creations/Noise/turbulence.nk").replace('\\', '/') + "\")")
m.addCommand('Creations/lines vertical', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Creations/Lines_Vertical.nk").replace('\\', '/') + "\")")
m.addCommand('Creations/lines horizontal', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Creations/Lines_Horizontal.nk").replace('\\', '/') + "\")")
m.addCommand('Creations/lines vertical animated', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Creations/Lines_Vertical_Animated.nk").replace('\\', '/') + "\")")
m.addCommand('Creations/lines horizontal animated', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Creations/Lines_Horizontal_Animated.nk").replace('\\', '/') + "\")")
m.addCommand('Creations/circles', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Creations/circles.nk").replace('\\', '/') + "\")")
m.addCommand('Creations/circles user', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Creations/circles_user.nk").replace('\\', '/') + "\")")
m.addCommand('Creations/points', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Creations/points.nk").replace('\\', '/') + "\")")
m.addCommand('Creations/points advanced', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Creations/points_advanced.nk").replace('\\', '/') + "\")")
m.addCommand('Creations/bricks', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Creations/bricks.nk").replace('\\', '/') + "\")")
m.addCommand('Creations/gradient horizontal', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Creations/gradient_horizontal.nk").replace('\\', '/') + "\")")
m.addCommand('Creations/gradient horizontal invert', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Creations/gradient_horizontal_invert.nk").replace('\\', '/') + "\")")
m.addCommand('Creations/gradient vertical', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Creations/gradient_vertical.nk").replace('\\', '/') + "\")")
m.addCommand('Creations/gradient vertical invert', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Creations/gradient_vertical_invert.nk").replace('\\', '/') + "\")")
m.addCommand('Creations/gradient 4 corners', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Creations/GradientCorner.nk").replace('\\', '/') + "\")")
m.addCommand('Creations/radial', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Creations/radial.nk").replace('\\', '/') + "\")")
m.addCommand('Creations/radial gradient', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Creations/radial_gradient.nk").replace('\\', '/') + "\")")
m.addCommand('Creations/radial rays', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Creations/radial_rays.nk").replace('\\', '/') + "\")")
m.addCommand('Creations/Trunc', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Creations/Trunc.nk").replace('\\', '/') + "\")")



#ALPHA
m.addCommand('Alpha/alpha binary', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Alpha/alpha_binary.nk").replace('\\', '/') + "\")")
m.addCommand('Alpha/alpha comparison', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Alpha/alpha_comparison.nk").replace('\\', '/') + "\")")
m.addCommand('Alpha/alpha exists?', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Alpha/alpha_exists.nk").replace('\\', '/') + "\")")
m.addCommand('Alpha/alpha sum', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Alpha/alpha_sum.nk").replace('\\', '/') + "\")")



#PIXEL
m.addCommand('Pixel/absolute value', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Pixel/abs.nk").replace('\\', '/') + "\")")
m.addCommand('Pixel/check negative', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Pixel/check_negative.nk").replace('\\', '/') + "\")")
m.addCommand('Pixel/check nan inf pixels', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Pixel/check_nan_inf.nk").replace('\\', '/') + "\")")
m.addCommand('Pixel/create nan pixel', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Pixel/create_nan.nk").replace('\\', '/') + "\")")
m.addCommand('Pixel/kill nan pixel', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Pixel/kill_nan.nk").replace('\\', '/') + "\")")
m.addCommand('Pixel/create inf pixel', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Pixel/create_inf.nk").replace('\\', '/') + "\")")
m.addCommand('Pixel/kill inf pixel', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Pixel/kill_inf.nk").replace('\\', '/') + "\")")



#TRANSFORM
m.addCommand('Transform/Coordinates', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Transform/coordinates.nk").replace('\\', '/') + "\")")
m.addCommand('Transform/UV Map', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Transform/UV_map.nk").replace('\\', '/') + "\")")
m.addCommand('Transform/UV to Vector', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Transform/UV_to_Vector.nk").replace('\\', '/') + "\")")
m.addCommand('Transform/Vector to UV', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Transform/Vector_to_UV.nk").replace('\\', '/') + "\")")
m.addCommand('Transform/transform', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Transform/transform.nk").replace('\\', '/') + "\")")
m.addCommand('Transform/transform advanced', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Transform/transform_advanced.nk").replace('\\', '/') + "\")")
m.addCommand('Transform/twist', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Transform/twist.nk").replace('\\', '/') + "\")")
m.addCommand('Transform/STMap_invert', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Transform/STMap_invert.nk").replace('\\', '/') + "\")")





#3D and DEEP
m.addCommand('3D and Deep/Normal Pass - Relight', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Deep_3D/normalPass_relight.nk").replace('\\', '/') + "\")")
m.addCommand('3D and Deep/C4x4', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Deep_3D/C4x4.nk").replace('\\', '/') + "\")")
m.addCommand('3D and Deep/Deep Thickness', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Deep_3D/deepThickness.nk").replace('\\', '/') + "\")")
m.addCommand('3D and Deep/Deep to Depth', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Deep_3D/deepToDepth.nk").replace('\\', '/') + "\")")
m.addCommand('3D and Deep/Deep from Depth', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Deep_3D/deepFromDepth.nk").replace('\\', '/') + "\")")
m.addCommand('3D and Deep/Depth normalize', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Deep_3D/depth_normalize.nk").replace('\\', '/') + "\")")



#KEYING and DESPILL
m.addCommand('Keying and Despill/despill green', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Keying_Despill/despill_green.nk").replace('\\', '/') + "\")")
m.addCommand('Keying and Despill/despill green list', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Keying_Despill/despill_green_list.nk").replace('\\', '/') + "\")")
m.addCommand('Keying and Despill/despill blue', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Keying_Despill/despill_blue.nk").replace('\\', '/') + "\")")
m.addCommand('Keying and Despill/despill blue list', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Keying_Despill/despill_blue_list.nk").replace('\\', '/') + "\")")
m.addCommand('Keying and Despill/keying', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Keying_Despill/keying.nk").replace('\\', '/') + "\")")
m.addCommand('Keying and Despill/differenceKey', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Keying_Despill/differenceKey.nk").replace('\\', '/') + "\")")
m.addCommand('Keying and Despill/IBKGizmo_Expression', "nuke.nodePaste(\"" + os.path.join(Expression_path, "Keying_Despill/IBKGizmo_Expression.nk").replace('\\', '/') + "\")")

m.addSeparator()


#INFO
m.addCommand('Info e Tutorial', "nuke.tcl('start', 'http://www.andreageremia.it/tutorial_expression_node.html')", icon = os.path.join(Expression_path, "icon/question_mark.png"))
