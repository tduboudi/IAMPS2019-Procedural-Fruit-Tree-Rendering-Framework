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

## Comments 


## Acknowledgements


## Credits




