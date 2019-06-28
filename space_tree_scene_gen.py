import bpy
import random as rd

###################################################################################
#Parameter to set the type of tree: 'a' for an apple tree or 'o' for an orange tree
###################################################################################
fruit_type = 'a'

############################
#Chooses the cycles renderer
############################
bpy.data.scenes['Scene'].render.engine = 'CYCLES'

############################################################################################
# removing all the objects (the default cube, lamp and camera) already existing in the scene
############################################################################################
for object in bpy.data.objects:
    object.select = True
bpy.ops.object.delete()

######################################
### architecture of generated tree ###
######################################
bpy.ops.object.group_instance_add('INVOKE_DEFAULT')

#################################################################################
#Create a dummy tree and delete it, so that the bark textures are properly loaded.
#################################################################################
bpy.ops.mesh.sca_tree(updateTree=True,
randomSeed=0,
maxIterations=100,
numberOfEndpoints=1000,
killDistance=1,
apicalcontrol=1,
apicalcontrolfalloff=15,
apicalcontroltiming=14,
newEndPointsPer1000=3,
addLeaves=True,
crownSize=5,
crownShape=1.25,
crownOffset=0.75,
noModifiers=False,
subSurface=True,
scale=0.02)

for object in bpy.data.objects:
    object.select = True
bpy.ops.object.delete()

#########################
#Creating the actual tree
#########################
bpy.ops.mesh.sca_tree(updateTree=True,
randomSeed=0,
maxIterations=100,
numberOfEndpoints=1000,
killDistance=1,
apicalcontrol=1,
apicalcontrolfalloff=15,
apicalcontroltiming=14,
newEndPointsPer1000=3,
addLeaves=True,
crownSize=5,
crownShape=1.25,
crownOffset=0.75,
noModifiers=False,
subSurface=True,
scale=0.02,
barkMaterial='BarkBetter1.1')

bpy.data.objects['Tree.001'].name = 'Tree'

##########################################################
#importing the images of leaves as planes on the 2nd layer
##########################################################
bpy.context.scene.layers[0] = False
bpy.context.scene.layers[1] = True

#######################################
#enables 'import image as plane' add-on
#######################################
bpy.ops.wm.addon_enable(module='io_import_images_as_planes')

######################################################
#import the leaf images as planes on the 2nd layer,
#and scale them
######################################################
bpy.ops.import_image.to_plane(shader='SHADELESS', files=[{'name':
'./leaf_texture/green_leaves_PNG3668.png'}])

bpy.ops.import_image.to_plane(shader='SHADELESS', files=[{'name':
'./leaf_texture/green_leaves_PNG3638.png'}])

bpy.ops.import_image.to_plane(shader='SHADELESS', files=[{'name':
'./leaf_texture/autumn_leaves_PNG3609.webp'}])

bpy.ops.import_image.to_plane(shader='SHADELESS', files=[{'name':
'./leaf_texture/autumn_leaves_PNG3581.webp',}])

bpy.data.objects['green_leaves_PNG3638'].location[0] = 2
bpy.data.objects['autumn_leaves_PNG3609'].location[0] = 4
bpy.data.objects['autumn_leaves_PNG3581'].location[0] = 6

bpy.context.scene.layers[0] = True
bpy.context.scene.layers[1] = False

bpy.data.objects['autumn_leaves_PNG3609'].rotation_euler[2] = -3.14159265/2
bpy.data.objects['autumn_leaves_PNG3609'].dimensions = [0.50775,0.79030,0.00320]

bpy.data.objects['autumn_leaves_PNG3581'].rotation_euler[2] = -3.14159265/2
bpy.data.objects['autumn_leaves_PNG3581'].dimensions = [0.92812,0.34389,0.01836]

bpy.data.objects['green_leaves_PNG3638'].dimensions[0] = 0.45702
bpy.data.objects['green_leaves_PNG3638'].dimensions[1] = 1.01056
bpy.data.objects['green_leaves_PNG3638'].dimensions[2] = 0.01250

bpy.data.objects['green_leaves_PNG3668'].dimensions[0] = 0.39461
bpy.data.objects['green_leaves_PNG3668'].dimensions[1] = 1.00073
bpy.data.objects['green_leaves_PNG3668'].dimensions[2] = 0.00200

##################################################################
#add 4 different types of leaves as 4 particle systems to the tree
##################################################################
tree = bpy.data.objects['Tree']
tree.modifiers.new("Leaves1", type='PARTICLE_SYSTEM')
leaves_particle_system = tree.particle_systems[0]
leaves_particle_system.seed = 54
leaves_settings = leaves_particle_system.settings
leaves_settings.regrow_hair = True
leaves_settings.type = 'HAIR'
leaves_settings.use_advanced_hair = True
leaves_settings.hair_step = 5
leaves_settings.count = 250
leaves_settings.hair_length = 4
leaves_settings.emit_from = 'FACE'
leaves_settings.use_emit_random = True
leaves_settings.use_even_distribution = True
leaves_settings.distribution = 'RAND'
leaves_settings.userjit = 0
leaves_settings.jitter_factor = 1
leaves_settings.use_modifier_stack = True
leaves_settings.use_render_emitter = True
leaves_settings.render_type = 'OBJECT'
leaves_settings.dupli_group = bpy.data.objects['autumn_leaves_PNG3581']
leaves_settings.use_scale_dupli = False
leaves_settings.particle_size = 0.380
leaves_settings.size_random = 1

tree = bpy.data.objects['Tree']
tree.modifiers.new("Leaves2", type='PARTICLE_SYSTEM')
leaves_particle_system = tree.particle_systems[1]
leaves_particle_system.seed = 54
leaves_settings = leaves_particle_system.settings
leaves_settings.regrow_hair = True
leaves_settings.type = 'HAIR'
leaves_settings.use_advanced_hair = True
leaves_settings.hair_step = 5
leaves_settings.count = 500
leaves_settings.hair_length = 4
leaves_settings.emit_from = 'FACE'
leaves_settings.use_emit_random = True
leaves_settings.use_even_distribution = True
leaves_settings.distribution = 'RAND'
leaves_settings.userjit = 0
leaves_settings.jitter_factor = 1
leaves_settings.use_modifier_stack = True
leaves_settings.use_render_emitter = True
leaves_settings.render_type = 'OBJECT'
leaves_settings.dupli_group = bpy.data.objects['autumn_leaves_PNG3609']
leaves_settings.use_scale_dupli = False
leaves_settings.particle_size = 0.380
leaves_settings.size_random = 1

tree = bpy.data.objects['Tree']
tree.modifiers.new("Leaves3", type='PARTICLE_SYSTEM')
leaves_particle_system = tree.particle_systems[2]
leaves_particle_system.seed = 54
leaves_settings = leaves_particle_system.settings
leaves_settings.regrow_hair = True
leaves_settings.type = 'HAIR'
leaves_settings.use_advanced_hair = True
leaves_settings.hair_step = 5
leaves_settings.count = 1000
leaves_settings.hair_length = 4
leaves_settings.emit_from = 'FACE'
leaves_settings.use_emit_random = True
leaves_settings.use_even_distribution = True
leaves_settings.distribution = 'RAND'
leaves_settings.userjit = 0
leaves_settings.jitter_factor = 1
leaves_settings.use_modifier_stack = True
leaves_settings.use_render_emitter = True
leaves_settings.render_type = 'OBJECT'
leaves_settings.dupli_group = bpy.data.objects['green_leaves_PNG3638']
leaves_settings.use_scale_dupli = False
leaves_settings.particle_size = 0.380
leaves_settings.size_random = 1

tree = bpy.data.objects['Tree']
tree.modifiers.new("Leaves4", type='PARTICLE_SYSTEM')
leaves_particle_system = tree.particle_systems[3]
leaves_particle_system.seed = 54
leaves_settings = leaves_particle_system.settings
leaves_settings.regrow_hair = True
leaves_settings.type = 'HAIR'
leaves_settings.use_advanced_hair = True
leaves_settings.hair_step = 5
leaves_settings.count = 1000
leaves_settings.hair_length = 4
leaves_settings.emit_from = 'FACE'
leaves_settings.use_emit_random = True
leaves_settings.use_even_distribution = True
leaves_settings.distribution = 'RAND'
leaves_settings.userjit = 0
leaves_settings.jitter_factor = 1
leaves_settings.use_modifier_stack = True
leaves_settings.use_render_emitter = True
leaves_settings.render_type = 'OBJECT'
leaves_settings.dupli_group = bpy.data.objects['green_leaves_PNG3668']
leaves_settings.use_scale_dupli = False
leaves_settings.particle_size = 0.380
leaves_settings.size_random = 1

#############################
#add orange object on layer 3
#############################
bpy.ops.import_scene.obj(filepath='./fruit_model/orange_for_cycles.obj')

######################################################################################
#adding the displace modifiers to the orange to give it random variations in structure
######################################################################################
tex = bpy.data.textures.new("CLOUDS",type='CLOUDS')
ob = bpy.data.objects['Orange']
mod = ob.modifiers.new(name="TEXMOD", type="DISPLACE")
mod.texture = tex
bpy.data.objects['Orange'].modifiers['TEXMOD'].strength = 0.2

tex = bpy.data.textures.new("CLOUDS",type='CLOUDS')
mod = ob.modifiers.new(name="TEXMODG", type="DISPLACE")
mod.texture = tex
bpy.data.objects['Orange'].modifiers['TEXMODG'].strength = 0.03
bpy.data.objects['Orange'].modifiers['TEXMODG'].texture_coords = 'GLOBAL'

###########################################################
# to avoid seing the original orange in the rendered images
###########################################################
bpy.data.objects['Orange'].layers[2] = True
bpy.data.objects['Orange'].layers[0] = False
bpy.data.objects['Orange'].layers[1] = False
bpy.data.objects['Orange'].layers[3] = False

###############################
#adding apple object on layer 4
###############################
bpy.ops.import_scene.obj(filepath='./fruit_model/apple_for_cycles.obj')

bpy.data.objects['pSphere6_Untitled.002'].name = 'Apple'

##########################################################
# to avoid seing the original apple in the rendered images
##########################################################
bpy.data.objects['Apple'].layers[3] = True
bpy.data.objects['Apple'].layers[0] = False
bpy.data.objects['Apple'].layers[1] = False
bpy.data.objects['Apple'].layers[2] = False

#####################################################################################
#adding the displace modifiers to the apple to give it random variations in structure
#####################################################################################
tex = bpy.data.textures.new("CLOUDS",type='CLOUDS')
ob = bpy.data.objects['Apple']
mod = ob.modifiers.new(name="TEXMOD", type="DISPLACE")
mod.texture = tex
bpy.data.objects['Apple'].modifiers['TEXMOD'].strength = 0.2

tex = bpy.data.textures.new("CLOUDS",type='CLOUDS')
mod = ob.modifiers.new(name="TEXMODG", type="DISPLACE")
mod.texture = tex
bpy.data.objects['Apple'].modifiers['TEXMODG'].strength = 0.03
bpy.data.objects['Apple'].modifiers['TEXMODG'].texture_coords = 'GLOBAL'

########################################
#adding oranges as particles on the tree
########################################
orange = bpy.data.objects['Orange']
tree.modifiers.new("Oranges", type='PARTICLE_SYSTEM')
oranges_particle_system = tree.particle_systems[4]
oranges_particle_system.seed = 0
oranges_settings = oranges_particle_system.settings
oranges_settings.regrow_hair = False
oranges_settings.type = 'HAIR'
oranges_settings.use_advanced_hair = True
oranges_settings.hair_step = 5
oranges_settings.count = 100
oranges_settings.hair_length = 4
oranges_settings.emit_from = 'VERT'
oranges_settings.use_emit_random = True
oranges_settings.use_even_distribution = True
oranges_settings.distribution = 'RAND'
oranges_settings.userjit = 0
oranges_settings.jitter_factor = 1
oranges_settings.use_modifier_stack = False
oranges_settings.use_render_emitter = True
oranges_settings.render_type = 'OBJECT'
oranges_settings.dupli_object = bpy.data.objects['Orange']
oranges_settings.use_scale_dupli = False
oranges_settings.particle_size = 0.120
oranges_settings.size_random = 0.364

#######################################
#adding apples as particles on the tree
#######################################
apple = bpy.data.objects['Apple']
tree.modifiers.new("Apples", type='PARTICLE_SYSTEM')
apples_particle_system = tree.particle_systems[5]
apples_particle_system.seed = 0
apples_settings = apples_particle_system.settings
apples_settings.regrow_hair = False
apples_settings.type = 'HAIR'
apples_settings.use_advanced_hair = True
apples_settings.hair_step = 5
apples_settings.count = 100
apples_settings.hair_length = 4
apples_settings.emit_from = 'VERT'
apples_settings.use_emit_random = True
apples_settings.use_even_distribution = True
apples_settings.distribution = 'RAND'
apples_settings.userjit = 0
apples_settings.jitter_factor = 1
apples_settings.use_modifier_stack = False
apples_settings.use_render_emitter = True
apples_settings.render_type = 'OBJECT'
apples_settings.dupli_object = bpy.data.objects['Apple']
apples_settings.use_scale_dupli = False
apples_settings.particle_size = 0.070
apples_settings.size_random = 0.364

########################################
#adding softbody modifiers to the leaves
########################################
objects = ['autumn_leaves_PNG3581','autumn_leaves_PNG3609',
'green_leaves_PNG3638','green_leaves_PNG3668']

for object in objects:
    ob = bpy.data.objects[object]
    mod = ob.modifiers.new(name="SB", type="SOFT_BODY")

################################
#Setting up nodes for the leaves
################################
for object in objects:
    leaf = bpy.data.objects[object]
    leaf_material = bpy.data.materials[object]
    leaf_material.use_nodes = True
    leaf_nodes = leaf_material.node_tree.nodes

    ##########################
    #delete all existing nodes
    ##########################
    for node in leaf_nodes:
        leaf_nodes.remove(node)

    node = leaf_nodes.new("ShaderNodeTexImage")
    node.name = "Image Texture"
    if object[0] == 'a':
        leaf_texture_image = bpy.data.images.load('./leaf_texture/' + object + '.webp')
    else:
        leaf_texture_image = bpy.data.images.load('./leaf_texture/' + object + '.png')

    leaf_material.node_tree.nodes["Image Texture"].image = leaf_texture_image

    node = leaf_nodes.new("ShaderNodeHueSaturation")
    node.name = "HSV"
    leaf_material.node_tree.nodes["HSV"].inputs[0].default_value = 0.5
    leaf_material.node_tree.nodes['HSV'].inputs[1].default_value = 0
    leaf_material.node_tree.nodes['HSV'].inputs[2].default_value = 1
    leaf_material.node_tree.nodes['HSV'].inputs[3].default_value = 1

    node = leaf_nodes.new("ShaderNodeBrightContrast")
    node.name = "Bright Contrast"

    leaf_material.node_tree.nodes['Bright Contrast'].inputs[1].default_value = -3.3
    leaf_material.node_tree.nodes['Bright Contrast'].inputs[2].default_value = 14

    node = leaf_nodes.new("ShaderNodeMath")
    node.name = "Math Multiply"
    leaf_material.node_tree.nodes['Math Multiply'].operation = 'MULTIPLY'

    node = leaf_nodes.new("ShaderNodeValToRGB")
    node.name = "Color Ramp"

    leaf_material.node_tree.nodes['Color Ramp'].color_ramp.elements[0].position = 0
    leaf_material.node_tree.nodes['Color Ramp'].color_ramp.elements[0].color[0] = 0.002
    leaf_material.node_tree.nodes['Color Ramp'].color_ramp.elements[0].color[1] = 0.099
    leaf_material.node_tree.nodes['Color Ramp'].color_ramp.elements[0].color[2] = 0.000

    leaf_material.node_tree.nodes['Color Ramp'].color_ramp.elements[1].position = 1
    leaf_material.node_tree.nodes['Color Ramp'].color_ramp.elements[1].color[0] = 0.123
    leaf_material.node_tree.nodes['Color Ramp'].color_ramp.elements[1].color[1] = 0.083
    leaf_material.node_tree.nodes['Color Ramp'].color_ramp.elements[1].color[2] = 0.009

    node = leaf_nodes.new("ShaderNodeBump")
    node.name = "Bump"

    leaf_material.node_tree.nodes['Bump'].inputs[0].default_value = 1
    leaf_material.node_tree.nodes['Bump'].inputs[1].default_value = 0.1

    node = leaf_nodes.new("ShaderNodeBsdfGlossy")
    node.name = "Glossy BSDF"

    leaf_material.node_tree.nodes['Glossy BSDF'].distribution = 'GGX'
    leaf_material.node_tree.nodes['Glossy BSDF'].inputs[0].default_value[0] = 0.8
    leaf_material.node_tree.nodes['Glossy BSDF'].inputs[0].default_value[1] = 0.8
    leaf_material.node_tree.nodes['Glossy BSDF'].inputs[0].default_value[2] = 0.8
    leaf_material.node_tree.nodes['Glossy BSDF'].inputs[1].default_value = 0.333

    node = leaf_nodes.new("ShaderNodeBsdfDiffuse")
    node.name = "Diffuse BSDF"
    leaf_material.node_tree.nodes['Diffuse BSDF'].inputs[1].default_value = 0.950

    node = leaf_nodes.new("ShaderNodeBsdfTransparent")
    node.name = "Transparent BSDF"
    leaf_material.node_tree.nodes['Transparent BSDF'].inputs[0].default_value[0] = 1
    leaf_material.node_tree.nodes['Transparent BSDF'].inputs[0].default_value[1] = 1
    leaf_material.node_tree.nodes['Transparent BSDF'].inputs[0].default_value[2] = 1

    node = leaf_nodes.new("ShaderNodeBsdfTranslucent")
    node.name = "Translucent BSDF"

    node = leaf_nodes.new("ShaderNodeMixShader")
    node.name = "Mix Shader"

    leaf_material.node_tree.nodes['Mix Shader'].inputs[0].default_value = 0.082

    node = leaf_nodes.new("ShaderNodeAddShader")
    node.name = "Add Shader"

    node = leaf_nodes.new("ShaderNodeMixShader")
    node.name = "Mix Shader1"

    node = leaf_nodes.new("ShaderNodeOutputMaterial")
    node.name = "Material Output"

    #############################
    #Connecting the created nodes
    #############################
    output = leaf_nodes['Image Texture'].outputs['Color']
    input = leaf_nodes['HSV'].inputs['Color']
    leaf_material.node_tree.links.new(output, input)

    input = leaf_nodes['Bump'].inputs['Height']
    leaf_material.node_tree.links.new(output,input)

    input = leaf_nodes['Translucent BSDF'].inputs['Color']
    leaf_material.node_tree.links.new(output,input)

    output = leaf_nodes['HSV'].outputs['Color']
    input = leaf_nodes['Bright Contrast'].inputs['Color']
    leaf_material.node_tree.links.new(output,input)

    output = leaf_nodes['Bright Contrast'].outputs[0]
    input = leaf_nodes['Math Multiply'].inputs[0]
    leaf_material.node_tree.links.new(output,input)

    output = leaf_nodes['Mix Shader1'].outputs['Shader']
    input = leaf_nodes['Material Output'].inputs['Surface']
    leaf_material.node_tree.links.new(output,input)

    output = leaf_nodes['Color Ramp'].outputs['Color']
    input = leaf_nodes['Math Multiply'].inputs[1]
    leaf_material.node_tree.links.new(output,input)

    output = leaf_nodes['Math Multiply'].outputs[0]
    input = leaf_nodes['Diffuse BSDF'].inputs['Color']
    leaf_material.node_tree.links.new(output,input)

    output = leaf_nodes['Diffuse BSDF'].outputs['BSDF']
    input = leaf_nodes['Mix Shader'].inputs[1]
    leaf_material.node_tree.links.new(output,input)

    output = leaf_nodes['Mix Shader'].outputs[0]
    input = leaf_nodes['Add Shader'].inputs[1]
    leaf_material.node_tree.links.new(output,input)

    output = leaf_nodes['Add Shader'].outputs['Shader']
    input = leaf_nodes['Mix Shader1'].inputs[2]
    leaf_material.node_tree.links.new(output,input)

    output = leaf_nodes['Translucent BSDF'].outputs['BSDF']
    input = leaf_nodes['Add Shader'].inputs[0]
    leaf_material.node_tree.links.new(output,input)

    output = leaf_nodes['Bump'].outputs['Normal']
    input = leaf_nodes['Diffuse BSDF'].inputs['Normal']
    leaf_material.node_tree.links.new(output,input)

    input = leaf_nodes['Glossy BSDF'].inputs['Normal']
    leaf_material.node_tree.links.new(output,input)

    input = leaf_nodes['Translucent BSDF'].inputs['Normal']
    leaf_material.node_tree.links.new(output,input)

    output = leaf_nodes['Bright Contrast'].outputs[0]
    input = leaf_nodes['Math Multiply'].inputs[0]

    output = leaf_nodes['Image Texture'].outputs['Alpha']
    input = leaf_nodes['Mix Shader1'].inputs[0]
    leaf_material.node_tree.links.new(output,input)

    output = leaf_nodes['Glossy BSDF'].outputs['BSDF']
    input = leaf_nodes['Mix Shader'].inputs[2]
    leaf_material.node_tree.links.new(output,input)

    output = leaf_nodes['Transparent BSDF'].outputs['BSDF']
    input = leaf_nodes['Mix Shader1'].inputs[1]
    leaf_material.node_tree.links.new(output,input)

###############################
#setting up nodes for the apple
###############################
parts_of_apple = ['phongE1','lambert2']

for part in parts_of_apple:

    apple = bpy.data.objects['Apple']
    apple_material = bpy.data.materials[part]
    apple_material.use_nodes = True
    apple_nodes = apple_material.node_tree.nodes

    node = apple_nodes.new("ShaderNodeTexImage")
    node.name = "Image Texture1"
    apple_texture_image = bpy.data.images.load('./fruit_model/Apple_Texture_by_AGF81.jpg')
    apple_material.node_tree.nodes["Image Texture1"].image = apple_texture_image

    node = apple_nodes.new("ShaderNodeTexImage")
    node.name = "Image Texture2"
    apple_texture_image = bpy.data.images.load('./fruit_model/Apple_Texture_by_AGF81.jpg')
    apple_material.node_tree.nodes["Image Texture2"].image = apple_texture_image
    apple_material.node_tree.nodes['Image Texture2'].color_space = 'NONE'

    #############################
    #Connecting the created nodes
    #############################
    output = apple_nodes['Image Texture1'].outputs[0]
    input = apple_nodes['Mix.002'].inputs[2]
    apple_material.node_tree.links.new(output,input)

    output = apple_nodes['Image Texture2'].outputs[0]
    input = apple_nodes['Normal Map'].inputs['Color']
    apple_material.node_tree.links.new(output,input)

    if part == "lambert2":

            node = apple_nodes.new("ShaderNodeMapping")
            node.name = "Mapping1"
            apple_material.node_tree.nodes['Mapping1'].vector_type = 'TEXTURE'
            apple_material.node_tree.nodes['Mapping1'].scale[0] = 1
            apple_material.node_tree.nodes['Mapping1'].scale[1] = 1
            apple_material.node_tree.nodes['Mapping1'].scale[2] = 1
            apple_material.node_tree.nodes['Mapping1'].rotation[0] = 0
            apple_material.node_tree.nodes['Mapping1'].rotation[1] = 0
            apple_material.node_tree.nodes['Mapping1'].rotation[2] = 5
            apple_material.node_tree.nodes['Mapping1'].translation[0] = 0
            apple_material.node_tree.nodes['Mapping1'].translation[1] = 1
            apple_material.node_tree.nodes['Mapping1'].translation[2] = 0

            #############################
            #Connecting the created nodes
            #############################
            output = apple_nodes['Mapping1'].outputs['Vector']
            input = apple_nodes['Image Texture1'].inputs['Vector']
            apple_material.node_tree.links.new(output,input)

            output = apple_nodes['Mapping1'].outputs['Vector']
            input = apple_nodes['Image Texture2'].inputs['Vector']
            apple_material.node_tree.links.new(output,input)

################################
#setting up nodes for the orange
################################
parts_of_orange = ['Skin','Stub']

for part in parts_of_orange:

    orange = bpy.data.objects['Orange']
    orange_material = bpy.data.materials[part]
    orange_material.use_nodes = True
    orange_nodes = orange_material.node_tree.nodes

    node = orange_nodes.new("ShaderNodeTexCoord")
    node.name = "Texture Coords"

    node = orange_nodes.new("ShaderNodeObjectInfo")
    node.name = "Object Info"

    node = orange_nodes.new("ShaderNodeValToRGB")
    node.name = "Color Ramp"

    node = orange_nodes.new("ShaderNodeMapping")
    node.name = "Mapping1"
    orange_material.node_tree.nodes['Mapping1'].vector_type = 'TEXTURE'

    node = orange_nodes.new("ShaderNodeMapping")
    node.name = "Mapping2"
    orange_material.node_tree.nodes['Mapping2'].vector_type = 'TEXTURE'

    node = orange_nodes.new("ShaderNodeTexImage")
    node.name = "Image Texture1"
    orange_texture_image = bpy.data.images.load('./fruit_model/Color.jpg')
    orange_material.node_tree.nodes["Image Texture1"].image = orange_texture_image


    node = orange_nodes.new("ShaderNodeTexImage")
    node.name = "Image Texture2"
    orange_texture_image = bpy.data.images.load('./fruit_model/Normal.jpg')
    orange_material.node_tree.nodes["Image Texture2"].image = orange_texture_image

    orange_material.node_tree.nodes['Mix.003'].inputs[1].default_value[0] = 1
    orange_material.node_tree.nodes['Mix.003'].inputs[1].default_value[1] = 0.689
    orange_material.node_tree.nodes['Mix.003'].inputs[1].default_value[2] = 0.155

    orange_material.node_tree.nodes['Image Texture2'].color_space = 'NONE'

    orange_material.node_tree.nodes['Color Ramp'].color_ramp.elements.new(position=0.5)

    orange_material.node_tree.nodes['Color Ramp'].color_ramp.elements[0].position = 0
    orange_material.node_tree.nodes['Color Ramp'].color_ramp.elements[0].color[0] = 0.319
    orange_material.node_tree.nodes['Color Ramp'].color_ramp.elements[0].color[1] = 0.125
    orange_material.node_tree.nodes['Color Ramp'].color_ramp.elements[0].color[2] = 0.015

    orange_material.node_tree.nodes['Color Ramp'].color_ramp.elements[1].position = 0.727
    orange_material.node_tree.nodes['Color Ramp'].color_ramp.elements[1].color[0] = 0.512
    orange_material.node_tree.nodes['Color Ramp'].color_ramp.elements[1].color[1] = 0.386
    orange_material.node_tree.nodes['Color Ramp'].color_ramp.elements[1].color[2] = 0.017

    orange_material.node_tree.nodes['Color Ramp'].color_ramp.elements[2].position = 1
    orange_material.node_tree.nodes['Color Ramp'].color_ramp.elements[2].color[0] = 0.220
    orange_material.node_tree.nodes['Color Ramp'].color_ramp.elements[2].color[1] = 0.314
    orange_material.node_tree.nodes['Color Ramp'].color_ramp.elements[2].color[2] = 0.027

    #############################
    #Connecting the created nodes
    #############################
    output = orange_nodes['Texture Coords'].outputs['UV']
    input = orange_nodes['Mapping1'].inputs['Vector']
    orange_material.node_tree.links.new(output,input)

    output = orange_nodes['Texture Coords'].outputs['UV']
    input = orange_nodes['Mapping2'].inputs['Vector']
    orange_material.node_tree.links.new(output,input)

    output = orange_nodes['Mapping1'].outputs['Vector']
    input = orange_nodes['Image Texture1'].inputs['Vector']
    orange_material.node_tree.links.new(output,input)

    output = orange_nodes['Mapping2'].outputs['Vector']
    input = orange_nodes['Image Texture2'].inputs['Vector']
    orange_material.node_tree.links.new(output,input)

    output = orange_nodes['Object Info'].outputs['Random']
    input = orange_nodes['Color Ramp'].inputs['Fac']
    orange_material.node_tree.links.new(output,input)

    output = orange_nodes['Texture Coords'].outputs['UV']
    input = orange_nodes['Mapping1'].inputs['Vector']
    orange_material.node_tree.links.new(output,input)

    output = orange_nodes['Color Ramp'].outputs[0]
    input = orange_nodes['Mix.002'].inputs[1]
    orange_material.node_tree.links.new(output,input)

    output = orange_nodes['Image Texture1'].outputs[0]
    input = orange_nodes['Mix.002'].inputs[2]
    orange_material.node_tree.links.new(output,input)

    output = orange_nodes['Image Texture2'].outputs[0]
    input = orange_nodes['Normal Map'].inputs['Color']
    orange_material.node_tree.links.new(output,input)


bpy.data.objects['Tree'].modifiers['Leaves.001'].name = 'Oranges'
bpy.data.objects['Tree'].modifiers['Oranges'].name = 'Apples'
bpy.data.objects['Tree'].modifiers['Apples'].name = 'None'

#######################################################################
#Setting the particles on the tree (apples or oranges) according to the
#'fruit_type' parameter
#######################################################################
if fruit_type == 'o':

    bpy.data.objects['Apple'].hide_render = True
    bpy.data.objects['Apple'].hide = True
    bpy.data.objects['Orange'].hide_render = False
    bpy.data.objects['Orange'].hide = False

else:

    bpy.data.objects['Apple'].hide_render = False
    bpy.data.objects['Apple'].hide = False
    bpy.data.objects['Orange'].hide_render = True
    bpy.data.objects['Orange'].hide = True


####################################
### Setup of ground truth labels ###
####################################

# what kind of supplementary information we want to create the labels
bpy.data.scenes["Scene"].render.layers["RenderLayer"].use_pass_z = True
bpy.data.scenes["Scene"].render.layers["RenderLayer"].use_pass_normal = True
bpy.data.scenes["Scene"].render.layers["RenderLayer"].use_pass_material_index = True

# Setup of the material index for the semantic segmentation label
bpy.data.materials["BarkBetter.001"].pass_index = 1
bpy.data.materials["Stub"].pass_index = 3
bpy.data.materials['Skin'].pass_index = 3
bpy.data.materials["autumn_leaves_PNG3581"].pass_index = 2
bpy.data.materials["autumn_leaves_PNG3609"].pass_index = 2
bpy.data.materials["green_leaves_PNG3638"].pass_index = 2
bpy.data.materials["green_leaves_PNG3668"].pass_index = 2

##########################################################################
# creation of a scene material
# no need to remove the existing nodes this time, we are going to use them
##########################################################################
bpy.data.scenes["Scene"].use_nodes = True
scene_nodes = bpy.data.scenes["Scene"].node_tree.nodes

# creation of all needed nodes
node = scene_nodes.new("CompositorNodeNormalize")
node.name = "Normalize Depth"

node = scene_nodes.new("CompositorNodeNormalize")
node.name = "Normalize Normal"

node = scene_nodes.new("CompositorNodeNormalize")
node.name = "Normalize Material Index"

node = scene_nodes.new("CompositorNodeValToRGB")
node.name = "Color Ramp Depth"
# nothing to change for the depth map color ramp

#####################################################################################
# creation of the node used for semantic segmentation labels
# the color_ramp.elements are used to define what color each type of
# object will be. (leaf -> blue, tree -> brown, fruit -> yellow, bakground -> black).
#####################################################################################
node = scene_nodes.new("CompositorNodeValToRGB")
node.name = "Color Ramp Normal"

node.color_ramp.elements.new(0.33)
node.color_ramp.elements[1].color[0] = 0
node.color_ramp.elements[1].color[1] = 0
node.color_ramp.elements[1].color[2] = 1
node.color_ramp.elements[1].color[3] = 1

node.color_ramp.elements.new(0.66)
node.color_ramp.elements[2].color[0] = 1
node.color_ramp.elements[2].color[1] = 0
node.color_ramp.elements[2].color[2] = 0
node.color_ramp.elements[2].color[3] = 1

node = scene_nodes.new("CompositorNodeValToRGB")
node.name = "Color Ramp Material Index"

node.color_ramp.elements[0].color[0] = 0
node.color_ramp.elements[0].color[1] = 0
node.color_ramp.elements[0].color[2] = 0
node.color_ramp.elements[0].color[3] = 1

node.color_ramp.elements.new(0.33)
node.color_ramp.elements[1].color[0] = 0.030
node.color_ramp.elements[1].color[1] = 0.013
node.color_ramp.elements[1].color[2] = 0.002
node.color_ramp.elements[1].color[3] = 1

node.color_ramp.elements.new(0.66)
node.color_ramp.elements[2].color[0] = 0
node.color_ramp.elements[2].color[1] = 0
node.color_ramp.elements[2].color[2] = 1
node.color_ramp.elements[2].color[3] = 1

node.color_ramp.elements[3].position = 0.870
node.color_ramp.elements[3].color[0] = 1
node.color_ramp.elements[3].color[1] = 1
node.color_ramp.elements[3].color[2] = 0
node.color_ramp.elements[3].color[3] = 1

node = scene_nodes.new("CompositorNodeOutputFile")
node.name = "File Output Depth"
node.base_path = './output/depth_map'

node = scene_nodes.new("CompositorNodeOutputFile")
node.name = "File Output Normal"
node.base_path = './output/normal_map'

node = scene_nodes.new("CompositorNodeOutputFile")
node.name = "File Output Material Index"
node.base_path = './output/segmentation_map'

##############################################################################
# linking of the nodes together (have a look a the nodes in the blender GUI to
# understand the function of each node)
##############################################################################
output = scene_nodes["Render Layers"].outputs['Depth']
input = scene_nodes["Normalize Depth"].inputs[0]
bpy.data.scenes["Scene"].node_tree.links.new(output, input)

output = scene_nodes["Render Layers"].outputs['Normal']
input = scene_nodes["Normalize Normal"].inputs[0]
bpy.data.scenes["Scene"].node_tree.links.new(output, input)

output = scene_nodes["Render Layers"].outputs['IndexMA']
input = scene_nodes["Normalize Material Index"].inputs[0]
bpy.data.scenes["Scene"].node_tree.links.new(output, input)

output = scene_nodes["Normalize Depth"].outputs[0]
input = scene_nodes["Color Ramp Depth"].inputs["Fac"]
bpy.data.scenes["Scene"].node_tree.links.new(output, input)

output = scene_nodes["Normalize Normal"].outputs[0]
input = scene_nodes["Color Ramp Normal"].inputs["Fac"]
bpy.data.scenes["Scene"].node_tree.links.new(output, input)

output = scene_nodes["Normalize Material Index"].outputs[0]
input = scene_nodes["Color Ramp Material Index"].inputs["Fac"]
bpy.data.scenes["Scene"].node_tree.links.new(output, input)

output = scene_nodes["Color Ramp Depth"].outputs["Image"]
input = scene_nodes["File Output Depth"].inputs[0]
bpy.data.scenes["Scene"].node_tree.links.new(output, input)

output = scene_nodes["Color Ramp Normal"].outputs["Image"]
input = scene_nodes["File Output Normal"].inputs[0]
bpy.data.scenes["Scene"].node_tree.links.new(output, input)

output = scene_nodes["Color Ramp Material Index"].outputs["Image"]
input = scene_nodes["File Output Material Index"].inputs[0]
bpy.data.scenes["Scene"].node_tree.links.new(output, input)

################################################
### setup of the background (HDRI) functions ###
################################################

# creation of a world material
bpy.data.worlds["World"].use_nodes = True
world_nodes = bpy.data.worlds["World"].node_tree.nodes

# removal of default nodes
for node in world_nodes:
    world_nodes.remove(node)

# creation of custom nodes
node = world_nodes.new("ShaderNodeTexEnvironment")
node.name = "Environment Texture"

node = world_nodes.new("ShaderNodeBackground")
node.name = "Background"

node = world_nodes.new("ShaderNodeOutputWorld")
node.name = "World Output"

# linking of the nodes together
output = world_nodes["Environment Texture"].outputs["Color"]
input = world_nodes["Background"].inputs["Color"]
bpy.data.worlds["World"].node_tree.links.new(output, input)

output = world_nodes["Background"].outputs["Background"]
input = world_nodes["World Output"].inputs["Surface"]
bpy.data.worlds["World"].node_tree.links.new(output, input)

# ( no need to chose the HDRI now )

##########################################################################
### setup of the camera and the empty element used to point the camera ###
##########################################################################

bpy.ops.object.camera_add()
bpy.ops.object.empty_add(type='ARROWS')
bpy.data.objects["Camera"].constraints.new("TRACK_TO")
bpy.data.objects["Camera"].constraints["Track To"].target = bpy.data.objects["Empty"]
bpy.data.objects["Camera"].constraints["Track To"].track_axis='TRACK_NEGATIVE_Z'
bpy.data.objects["Camera"].constraints["Track To"].up_axis='UP_Y'

##########################################################################################
### setup of the rendering options that are not going to change during data generation ###
##########################################################################################

bpy.data.scenes["Scene"].cycles.device="CPU"
bpy.data.scenes["Scene"].render.resolution_x = 512
bpy.data.scenes["Scene"].render.resolution_y = 512
bpy.data.scenes["Scene"].render.resolution_percentage = 100
bpy.data.scenes["Scene"].render.use_overwrite = True
bpy.data.scenes["Scene"].render.use_file_extension = True
bpy.data.scenes["Scene"].cycles.samples = 32
bpy.data.scenes["Scene"].cycles.min_bounces = 3
bpy.data.scenes["Scene"].cycles.max_bounces = 9
bpy.data.scenes["Scene"].render.tile_x = 128
bpy.data.scenes["Scene"].render.tile_y = 128
bpy.data.scenes["Scene"].camera = bpy.data.objects["Camera"]
