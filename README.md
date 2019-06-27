# IAMPS2019-Procedural-Fruit-Tree-Rendering-Framework

Code to accompany the IAMPS 2019 paper "Toward a procedural fruit tree rendering framework for image analysis"

Source code authors : Thomas Duboudin, Maxime Petit, Sridhar Ragupathi, Liming Chen

This code allows you to reproduce the results of the IAMPS 2019 paper "Toward a procedural fruit tree rendering framework for image analysis".

## Installation instructions

(On Ubuntu 18.04)

1 - Download and install Blender (https://www.blender.org/). We are aware of problems with the gpu-rendering options on Blender 2.79b, thus, by default, it's the CPU rendering that is enabled. It's possible to switch the option to GPU in the scene generation scripts, at the end of each of the scripts. To enable GPU-rendering, follow this link : https://docs.blender.org/manual/en/dev/render/cycles/gpu_rendering.html.

2 - Install the Blender Add-on "Sapling Tree Gen". To do so, go to "File" -> "User preferences" -> "Add-ons" and search for "Sapling Tree Gen" in the research toolbar. Click on the tick-box and save the setting at the bottom of the window.

3 - Install the "spacetree" Add-on, to do so : go to https://github.com/varkenvarken/spacetree and follow the installation instructions. It's an older Add-on no longer by default on Blender, you'll need to download a zip file and import it in Blender.

4 - (if needed) Download the textures and additional files from the following links and put them in the corresponding folder. There is already a few files for a plug-and-play example :

-- HDRIs (360° high-resolution background image) : https://hdrihaven.com/

-- Leaves textures : http://pngimg.com/, https://www.textures.com/

-- Bark texture : https://www.textures.com/

-- Fruit 3D models & texture : https://www.turbosquid.com/, https://free3d.com/3d-models/

5 - Download the repository archive or clone it.

6 - Open the Blender GUI and choose the "Scripting" panel configuration (in the top toolbar, next to "Help", it should be at default initially).

7 - Open the scene generation script and launch it.

8 - Open the rendering script and launch it.

## Some examples of generated images

![Alt text](relative/path/to/img.jpg?raw=true "Title")
![Alt text](relative/path/to/img.jpg?raw=true "Title")
![Alt text](relative/path/to/img.jpg?raw=true "Title")
![Alt text](relative/path/to/img.jpg?raw=true "Title")
![Alt text](relative/path/to/img.jpg?raw=true "Title")

## Comments 

==> You can change the rendering parameters and the scene parameters in the corresponding scripts. In particular, if you're designing a new tree model, don't forget to change the camera movement parameters (the inner box for the empty element and the outer cylinder for the camera).

==> If you're willing to create more complex models and need more blender knowledge, check the tutorials by Blender Guru.

==> We cannot easily make sure that the leaves are attached to the branches by their tails, nor that there won't be fruits and leaves intersecting themselves. This is linked to the fruits and leaves generation as random particles on the tree structure. We do not believe it is going to be a major issue with our data, since complete photorealism does not seem to be needed (cf paper) for deep learning. Furthermore, there is a trade-off between the time spent designing a model and the amout of variations we can put in the rendered images.



## Acknowledgements

This work is supported by the french National Research Agency (ANR), through the ARES labcom (grant ANR 16-LCV2-0012-01) and by the CHIST-ERA EU project "Learn-Real".

## Credits

The given HRDI : https://hdrihaven.com/hdri/?c=outdoor&h=spruit_sunrise

The given leaves textures : https://www.textures.com/download/leaves0089/21795?q=leaves, http://pngimg.com/download/3668, http://pngimg.com/download/3638, http://pngimg.com/download/3581, http://pngimg.com/download/3609

The given bark texture : https://www.textures.com/download/3dscans0062/127610?q=cedar+tree

The given orange object : https://www.turbosquid.com/3d-models/free-3ds-model-orange-resolution-photorealistic/756550

The given apple object : [TODO]





