import argparse
import os.path
import shutil
import subprocess

TheFolder = "A:\sad\\"
parser = argparse.ArgumentParser(description="Store and diff script. "
                                             "This thing can only store and compare any files. "
                                             "Type \"path-to-sad.py [command] path-to-file\". "
                                             "Command must be \"store\"(to store the file)"
                                             "or \"diff\"(to compare file with it's stored clone). "
                                             "Or launch with --help to get more info")
parser.add_argument("command",
                    type=str,
                    choices=["store", "diff"],
                    nargs="?",
                    help="type \"store\" or \"diff\"")

parser.add_argument('path',
                    type=str,
                    default="no path",
                    nargs="?",
                    help="full path to file")
args = parser.parse_args()
if args.command is None:
    print("Type a command!")
elif os.path.isfile(args.path) is False:
    print("File not found or path is not stated")
else:
    filename = args.path.split("\\")
    filename = filename[len(filename) - 1]
    if args.command == "store":
        shutil.copyfile(args.path, TheFolder + filename)
        print("stored!")
    elif args.command == "diff":
        if os.path.isfile(TheFolder + filename) is False:
            print("This file is not stored")
        else:
            subprocess.run("FC " + args.path + " " + TheFolder + filename)
