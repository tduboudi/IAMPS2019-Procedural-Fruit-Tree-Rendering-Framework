import bpy
import random as rd
import math as math
import os
import itertools

# This script is used to generate the images. It is meant to be used after the
# scene generation script. It controls parameters such as the number of images
# that are going to be rendered, the change frequency for the background images,
# the rendering quality, etc.

###################################
### Background image parameters ###
###################################

scene = bpy.context.scene
world = scene.world
nodes_tree = bpy.data.worlds[world.name].node_tree
env_text_node = nodes_tree.nodes["Environment Texture"]

# the folder in which all HDRIs files are located
hdri_folder = './hdri'

hdri_list = os.listdir(hdri_folder)
hdri_cycle_iterator = itertools.cycle(hdri_list)

# the background changes every change_frequency rendered images
change_frequency = 2

##########################################################
### Camera & render options & associated empty element ###
##########################################################

camera = bpy.data.objects['Camera']
empty = bpy.data.objects['Empty']

# the number of samples used for rendering (the higher the better the generated images)
bpy.data.scenes["Scene"].cycles.samples = 64

# Blender >2.79 only. used to further improve the images quality
# bpy.context.scene.render.layers[0].cycles.use_denoising = True

#####################################################
### Parameters of camera position and orientation ###
#####################################################

pi = 3.14159265

# definition of the 3D box the empty element (to which the camera is
# going to point toward) is going to be sampled from

x_range = [-5,5]
y_range = [-5,5]
z_range = [3,3]

# definition of the hollow cylinder the camera position is going to be sampled from

# height original
#h2 = 10
#h1 = 3
h2 = 8
h1 = 3
# radius original
#r1 = 3
#r2 = 10
r1 = 5
r2 = 6

############################
### Animation parameters ###
############################

# number of rendered images (change only ending_frame_num to modify the number
# of rendered images)
starting_frame_num = 1
ending_frame_num = 5000

bpy.data.scenes["Scene"].frame_end = ending_frame_num

#################
### MAIN LOOP ###
#################

for current_frame_num in range (starting_frame_num, ending_frame_num+1):

    # step forward in time
    bpy.context.scene.frame_set(current_frame_num)

    # random camera position parameters
    theta = rd.random()*2*pi
    alpha = rd.random()

    # modification of the camera location
    camera.location[0] = (r1+alpha*(r2-r1))*math.cos(theta)
    camera.location[1] = (r1+alpha*(r2-r1))*math.sin(theta)
    camera.location[2] = (h2-h1)*rd.random()+h1
    camera.rotation_euler[2] = camera.rotation_euler[2] + pi

    # recording the camera location at the current timestep
    camera.keyframe_insert(data_path='location', index=-1)

    # modification of the empty element location
    # because the camera is assigned to track this empty, it will modify
    # its orientation and make point toward the tree (with a random factor,
    # it will not always point toward the center of the tree)
    empty.location[0] = rd.random()*(x_range[1]-x_range[0])+x_range[0]
    empty.location[1] = rd.random()*(y_range[1]-y_range[0])+y_range[0]
    empty.location[2] = rd.random()*(z_range[1]-z_range[0])+z_range[0]

    empty.keyframe_insert(data_path='location', index=-1)

    # recording the camera orientation at the current timestep (making it
    # point toward the empty element location)
    camera.keyframe_insert(data_path='rotation_euler', index=-1)

    ## changing the background image (according to defined change_frequency)
    if current_frame_num % change_frequency == 1:
        current_hdri = next(hdri_cycle_iterator)
        current_bg_image = bpy.data.images.load(os.path.join(hdri_folder, current_hdri))
        env_text_node.image = current_bg_image
    else :
        env_text_node.image = current_bg_image

    # render and save the image
    # the labels are rendered automatically for each generated images (as defined
    # in the scene generation script)
    bpy.data.scenes['Scene'].render.filepath = './output/images/image_'+str(current_frame_num)
    bpy.ops.render.render(write_still=True)
