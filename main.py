from os import path
import argparse

parser = argparse.ArgumentParser(description="Read out a file's contents.")
parser.add_argument("file", help="the path to the file to output")
args = parser.parse_args()

if path.exists(args.file):
    with open(args.file, "r", encoding="utf-8") as f:
        print(f.read())
else:
    print("File doesn't exist!")
