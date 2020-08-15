# Convert CUBE LUT files for usage in Unreal
A utility script to batch convert CUBE LUT files for usage in UE4. Saves time rather than manually converting individual LUTs if you have an existing catalog or have bought a LUT pack like [IWLTBAP's Cinematic Pack](https://luts.iwltbap.com/)

## Instructions
1) Install Python 3.x
2) Run the following command
```bash
pip install pillow pillow_lot
```
3) Download/clone this project
4) Download the neutral RGB LUT from Epic and save it into the folder beside the .py file. [Source Page](https://docs.unrealengine.com/en-US/Engine/Rendering/PostProcessEffects/UsingLUTs/index.html), [Direct  Image Link](https://docs.unrealengine.com/Images/Engine/Rendering/PostProcessEffects/UsingLUTs/RGBTable16x1.png) 
5) Run the script with a directory containing LUT files. Nested directories are ok and it will convert every CUBE file found.
```bash
python cube_to_ue4_lut_conversion.py <directory of luts>
```

6) Import the desired PNG into Unreal, and change the texture group to ColorLookupTable.

For more information on using LUTs in unreal see the [documentation here](https://docs.unrealengine.com/en-US/Engine/Rendering/PostProcessEffects/UsingLUTs/index.html)
