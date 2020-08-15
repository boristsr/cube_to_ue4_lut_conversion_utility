# Convert CUBE LUT files for usage in Unreal
A utility script to convert CUBE LUT files for usage in UE4.

## Instructions
1) Install Python 3.x
2) Run the following command
```bash
pip install pillow pillow_lot
```
3) Download/clone this project
4) Download the neutral RGB LUT from Epic [Source Page](https://docs.unrealengine.com/en-US/Engine/Rendering/PostProcessEffects/UsingLUTs/index.html) [Direct Link](https://docs.unrealengine.com/Images/Engine/Rendering/PostProcessEffects/UsingLUTs/RGBTable16x1.png) and save it into the folder beside the .py file.
5) Run the script with a directory containing LUT files. Nested directories are ok and it will convert every CUBE file found.
```bash
python cube_to_ue4_lut_conversion.py <directory of luts>
```

6) Import the desired PNG into Unreal, and change the texture group to ColorLookupTable.

For more information on using LUTs in unreal see the [documentation here](https://docs.unrealengine.com/en-US/Engine/Rendering/PostProcessEffects/UsingLUTs/index.html)
