from PIL import Image, ImageOps
from pathlib import Path

# if __name__ == "__main__":
input_folder = Path("content/input_images")

directories = list(input_folder.iterdir())
print(directories)