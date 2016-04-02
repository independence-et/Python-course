import argparse
import os.path
import subprocess

parser = argparse.ArgumentParser(description="image_shrinker")
parser.add_argument("percent",
                    type=int,
                    help="percentage you need to shrink")

parser.add_argument('path',
                    type=str,
                    default="no path",
                    nargs="?",
                    help="full path to file")
parser.add_argument('new_path',
                    type=str,
                    nargs="?")
args = parser.parse_args()
def press(path1, path2):
    subprocess.run("convert " + path1 + " -resize " + str(args.percent) + "% " + path2, shell=True)
if os.path.isdir(args.path) == True:
    pathes = list()
    for d, dirs, files in os.walk(args.path):
        for f in files:
            x = os.path.join(d, f)
            pathes.append(x)
    for file in pathes:
        type = file.split(".")[1]
        if type == "png" or type == "jpg":
            press(file, file)
elif os.path.isfile(args.path) == False:
    print("File not found or path is not stated")
else:
    if args.new_path is None:
        args.new_path = args.path
    press(args.path, args.new_path)
