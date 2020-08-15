import os
import sys

import pillow_lut
from PIL import Image

def convert_lut(src_lut_path, neutral_image_path, out_path):
    src_lut_file = open(src_lut_path)
    lines = src_lut_file.readlines()
    src_lut = pillow_lut.load_cube_file(lines)
    neutral_image = Image.open(neutral_image_path)
    LUT_applied_image = neutral_image.filter(src_lut)
    LUT_applied_image.save(out_path)

def convert_all_luts_in_directory(root_path):
    print("Finding all .CUBE files in: " + root_path)
    for dirpath, dnames, fnames in os.walk(root_path):
        for f in fnames:
            if f.lower().endswith(".cube"):
                print("Converting: " + f)
                src_lut_path = os.path.join(dirpath, f)
                out_path = src_lut_path + ".PNG"
                neutral_image_path = "RGBTable16x1.png"
                convert_lut(src_lut_path, neutral_image_path, out_path)

def print_help():
    print("Converts .CUBE LUT files into a format suitable for usage in UE4")
    print()
    print("Usage: python cube_to_ue4_lut_conversion.py <directory of luts>")
    print()
    print("To use this script, please supply a directory containing .CUBE LUT files.")
    print("The resulting PNG files, suitable for use in UE4 will be placed beside the original .CUBE file with a .PNG extension")
    print()
    print("If your path has spaces, enclose in quotes as in the example below.")
    print()
    print("Usage examples:")
    print("\tpython cube_to_ue4_lut_conversion.py d:\\luts")
    print("\tpython cube_to_ue4_lut_conversion.py \"c:\\users\\some user\\desktop\\luts\"")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_help()
    else:
        process_path = sys.argv[1]
        process_path = os.path.normpath(process_path)
        convert_all_luts_in_directory(process_path)