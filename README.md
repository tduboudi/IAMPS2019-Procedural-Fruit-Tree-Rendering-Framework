# IAMPS2019-Procedural-Fruit-Tree-Rendering-Framework

Code to accompany the IAMPS 2019 paper "Toward a procedural fruit tree rendering framework for image analysis"

Source code authors : Thomas Duboudin, Maxime Petit, Sridhar Ragupathi, Liming Chen

This code allows you to reproduce the results of the IAMPS 2019 paper "Toward a procedural fruit tree rendering framework for image analysis".

To use the source code :

1 - Download and install Blender (https://www.blender.org/). We recommand using Blender 2.78c instead of Blender 2.79b (the latest as of 27/06/19) as we had problems getting the GPU-rendering to work with the latest version and a GTX NVIDIA 1080. To enable GPU-rendering, follow this link : https://docs.blender.org/manual/en/dev/render/cycles/gpu_rendering.html.

2 - Install the Blender Add-on "Sapling Tree Gen". To do so, go to "File" -> "User preferences" -> "Add-ons" and search for "Sapling Tree Gen" in the research toolbar. Install the "spacetree" Add-on, to do so : go to https://github.com/varkenvarken/spacetree and follow the installation instructions.

3 - Download the textures and additional files from the following links and put them in the corresponding folder (there is already a few files for a plug-and-play example) :

-- HDRIs (360° high-resolution background image) : https://hdrihaven.com/ (as many as you want)

-- Leaves textures : http://pngimg.com/download/3668
                     http://pngimg.com/download/3638
                     http://pngimg.com/download/3581 
                     http://pngimg.com/download/3609

-- Bark texture : 

-- Fruit texture : 

-- Fruit 3D models : 

4 - Download the repository archive or clone it.

5 - Open the Blender GUI and choose the "Scripting" panel configuration (in the top toolbar, next to "Help", it should be at default initially).

6 - Open the scene generation script and launch it. Change the paths if needed.

7 - Open the rendering script and launch it. Change the saving paths if needed.

8 - you're done !
