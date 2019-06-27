### BLENDER SCENE GENERATION SCRIPT ###

import bpy
import random as rd

# using the cycles rendering engine

bpy.data.scenes['Scene'].render.engine = 'CYCLES'

# removing all the objects already existing in the scene

for object in bpy.data.objects:
    object.select = True
bpy.ops.object.delete()

# architecture of generated tree

bpy.ops.curve.tree_add(do_update=True,
                        bevel=True,
                        prune=False,
                        showLeaves=True,
                        useArm=False,
                        seed=0,
                        handleType='0',
                        levels=rd.randint(3, 4),
                        length=(1, 0.3, 0.6, 0.45),
                        lengthV=(0, 0, 0, 0),
                        taperCrown=0,
                        branches=(0, 50, 30, 10),
                        curveRes=(8, 5, 3, 1),
                        curve=(0, -40, -40, 0),
                        curveV=(20, 50, 75, 0),
                        curveBack=(0, 0, 0, 0),
                        baseSplits=0,
                        segSplits=(0, 0, 0, 0),
                        splitByLen=True,
                        rMode='rotate',
                        splitAngle=(0, 0, 0, 0),
                        splitAngleV=(0, 0, 0, 0),
                        scale=13,
                        scaleV=3,
                        attractUp=(0, 0, 0.5, 0.5),
                        attractOut=(0, 0, 0, 0),
                        shape='1',
                        shapeS='1',
                        customShape=(0.5, 1, 0.3, 0.5),
                        branchDist=1,
                        nrings=0,
                        baseSize=rd.uniform(0.1, 0.4),
                        baseSize_s=0.25,
                        splitHeight=rd.uniform(0.1, 0.2),
                        splitBias=rd.uniform(0.0, 1.0),
                        ratio=0.015,
                        minRadius=0.0015,
                        closeTip=False,
                        rootFlare=1,
                        autoTaper=True,
                        taper=(1, 1, 1, 1),
                        radiusTweak=(1, 1, 1, 1),
                        ratioPower=1.1,
                        downAngle=(90, 110, 45, 45),
                        downAngleV=(0, 80, 10, 10),
                        useOldDownAngle=False,
                        useParentAngle=True,
                        rotate=(99.5, 137.5, 137.5, 137.5),
                        rotateV=(rd.randint(-30, 30), rd.randint(-30, 30), rd.randint(-30, 30), rd.randint(-30, 30)),
                        scale0=1,
                        scaleV0=0.1,
                        pruneWidth=0.4,
                        pruneBase=0.3,
                        pruneWidthPeak=0.6,
                        prunePowerHigh=0.5,
                        prunePowerLow=0.001,
                        pruneRatio=1,
                        leaves=rd.randint(25, 50),
                        leafDownAngle=45,
                        leafDownAngleV=10,
                        leafRotate=137.5,
                        leafRotateV=0,
                        leafScale=0.17,
                        leafScaleX=1,
                        leafScaleT=0,
                        leafScaleV=0,
                        leafShape='hex',
                        leafangle=0,
                        horzLeaves=True,
                        leafDist=rd.choice(['1', '2', '3', '4', '5', '6', '7']),
                        bevelRes=0,
                        resU=4,
                        armAnim=False,
                        previewArm=False,
                        leafAnim=False,
                        frameRate=1,
                        loopFrames=0,
                        wind=1,
                        gust=1,
                        gustF=0.075,
                        af1=1,
                        af2=1,
                        af3=4,
                        makeMesh=False,
                        armLevels=2,
                        boneStep=(1, 1, 1, 1))

# textures and materials of generated tree

## leaves

leaf_material = bpy.data.materials.new("LEAF_material")
leaf_material.use_nodes = True
leaf_nodes = leaf_material.node_tree.nodes

for node in leaf_nodes:
    leaf_nodes.remove(node)

node = leaf_nodes.new("ShaderNodeTexImage")
node.name = "Image Texture"

node = leaf_nodes.new("ShaderNodeInvert")
node.name = "Invert"

node = leaf_nodes.new("ShaderNodeBsdfDiffuse")
node.name = "Diffuse BSDF"

node = leaf_nodes.new("ShaderNodeBsdfTransparent")
node.name = "Transparent BSDF"

node = leaf_nodes.new("ShaderNodeAddShader")
node.name = "Add Shader"

node = leaf_nodes.new("ShaderNodeOutputMaterial")
node.name = "Material Output"

output = leaf_nodes['Image Texture'].outputs['Alpha']
input = leaf_nodes['Invert'].inputs['Color']
leaf_material.node_tree.links.new(output, input)

output = leaf_nodes['Image Texture'].outputs['Color']
input = leaf_nodes['Diffuse BSDF'].inputs['Color']
leaf_material.node_tree.links.new(output, input)

output = leaf_nodes['Invert'].outputs['Color']
input = leaf_nodes['Transparent BSDF'].inputs['Color']
leaf_material.node_tree.links.new(output, input)

output = leaf_nodes['Diffuse BSDF'].outputs['BSDF']
input = leaf_nodes['Add Shader'].inputs[0]
leaf_material.node_tree.links.new(output, input)

output = leaf_nodes['Transparent BSDF'].outputs['BSDF']
input = leaf_nodes['Add Shader'].inputs[1]
leaf_material.node_tree.links.new(output, input)

output = leaf_nodes['Add Shader'].outputs['Shader']
input = leaf_nodes['Material Output'].inputs['Surface']
leaf_material.node_tree.links.new(output, input)

leaf_texture_image = bpy.data.images.load("./leaf_texture/TexturesCom_Leaves0089_1_masked_S.png")
bpy.data.materials['LEAF_material'].node_tree.nodes["Image Texture"].image = leaf_texture_image

bpy.data.objects['leaves'].active_material = leaf_material

## trunk and branches

wood_material = bpy.data.materials.new("WOOD_material")
wood_material.use_nodes = True
wood_nodes = wood_material.node_tree.nodes

for node in wood_nodes:
    wood_nodes.remove(node)

node = wood_nodes.new("ShaderNodeTexImage")
node.name = "Image Texture"

node = wood_nodes.new("ShaderNodeBsdfDiffuse")
node.name = "Diffuse BSDF"

node = wood_nodes.new("ShaderNodeOutputMaterial")
node.name = "Material Output"

output = wood_nodes["Image Texture"].outputs['Color']
input = wood_nodes["Diffuse BSDF"].inputs['Color']
wood_material.node_tree.links.new(output, input)

output = wood_nodes["Diffuse BSDF"].outputs["BSDF"]
input = wood_nodes["Material Output"].inputs['Surface']
wood_material.node_tree.links.new(output, input)

wood_texture_image = bpy.data.images.load("./bark_texture/TexturesCom_CedarTreeBark_1K_albedo.tif")
bpy.data.materials["WOOD_material"].node_tree.nodes["Image Texture"].image = wood_texture_image

bpy.data.objects['tree'].active_material = wood_material

# fruits as a particle system

bpy.ops.import_scene.obj(filepath='./fruit_model/orange_for_cycles.obj')

# to avoid seing the original fruit in the rendered images
bpy.data.objects['Orange'].layers[1] = True
bpy.data.objects['Orange'].layers[0] = False

leaves = bpy.data.objects['leaves']
leaves.modifiers.new("FRUITS", type='PARTICLE_SYSTEM')
fruits_particle_system = leaves.particle_systems[0]
fruits_settings = fruits_particle_system.settings

fruits_settings.type = "HAIR"
fruits_settings.use_advanced_hair = True
fruits_settings.hair_step = 5
fruits_settings.count = 500
fruits_settings.hair_length = 2.5
fruits_settings.emit_from = "FACE"
fruits_settings.use_emit_random = True
fruits_settings.use_even_distribution=True
fruits_settings.distribution = "JIT"
fruits_settings.use_rotations = True
fruits_settings.rotation_mode = "NOR_TAN"
fruits_settings.rotation_factor_random = 0.5
fruits_settings.phase_factor = -0.4
fruits_settings.phase_factor_random = 1.3
fruits_settings.render_type = "OBJECT"
fruits_settings.dupli_object = bpy.data.objects['Orange']



# setup of the HDRI functions

bpy.data.worlds["World"].use_nodes = True
world_nodes = bpy.data.worlds["World"].node_tree.nodes
for node in world_nodes:
    world_nodes.remove(node)

node = world_nodes.new("ShaderNodeTexEnvironment")
node.name = "Environment Texture"

node = world_nodes.new("ShaderNodeBackground")
node.name = "Background"

node = world_nodes.new("ShaderNodeOutputWorld")
node.name = "World Output"

output = world_nodes["Environment Texture"].outputs["Color"]
input = world_nodes["Background"].inputs["Color"]
bpy.data.worlds["World"].node_tree.links.new(output, input)

output = world_nodes["Background"].outputs["Background"]
input = world_nodes["World Output"].inputs["Surface"]
bpy.data.worlds["World"].node_tree.links.new(output, input)

# ( no need to chose the HDRI now )

# setup of the camera and the empty element used to point the camera

bpy.ops.object.camera_add()
bpy.ops.object.empty_add(type='ARROWS')
bpy.data.objects["Camera"].constraints.new("TRACK_TO")
bpy.data.objects["Camera"].constraints["Track To"].target = bpy.data.objects["Empty"]
bpy.data.objects["Camera"].constraints["Track To"].track_axis='TRACK_NEGATIVE_Z'
bpy.data.objects["Camera"].constraints["Track To"].up_axis='UP_Y'

# setup of the rendering options that are not going to change during data generation

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
