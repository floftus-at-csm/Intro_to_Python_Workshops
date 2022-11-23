from PIL import Image, ImageOps
from pathlib import Path

def convert_image_to_jpg(img):
    new_img = Image.new("RGB", img.size, (255, 255, 255))
    new_img.paste(img, mask=img.split()[3]) # 3 is the alpha channel
    return new_img

input_folder = Path("input_images")
output_folder = Path("output_images")

file_to_open = input_folder / "morehshin.png"
im1 = Image.open(file_to_open) 
  
# image segmentation 
# using threshold value = 130
# applying solarize method 
try:
    im2 = ImageOps.solarize(im1, threshold = 130) 
except:
    im1 = convert_image_to_jpg(im1)
    im2 = ImageOps.solarize(im1, threshold = 130)

# im2.show()
output_path = output_folder / "test.jpg"
im2.save(output_path)