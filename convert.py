import argparse
from PIL import Image

parser = argparse.ArgumentParser(description="Simple CLI image converter")
parser.add_argument("--file", type=str, help="Required arg: filename")
parser.add_argument("--type", type=str, help="A required argument: state which file type you want to convert it to")

# parse the arguments
args = parser.parse_args()
old_image = Image.open(args.file)
if not old_image.mode == "RGB":
    # convert to RGB
    old_image = old_image.convert("RGB")

old_image.save(args.file[:len(file)-3] + args.type)
