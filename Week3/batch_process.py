from PIL import Image, ImageOps
from pathlib import Path

def convert_image_to_jpg(img):
    # This function converts a png image to a jpg
    new_img = Image.new("RGB", img.size, (255, 255, 255))
    new_img.paste(img, mask=img.split()[3]) # 3 is the alpha channel
    return new_img

if __name__ == "__main__":
    input_folder = Path("content/input_images")
    output_folder = Path("content/output_images")
    directories = list(input_folder.iterdir())
    print(directories)
    for count, item in enumerate(directories):
        im1 = Image.open(item) 
        try:
            im2 = ImageOps.solarize(im1, threshold = 130) 
        except:
            im1 = convert_image_to_jpg(im1)
            im2 = ImageOps.solarize(im1, threshold = 130)
            
        # im2.show()
        output_path = "content/output_images/" + str(count) + '.png'
        im2.save(output_path)
        print("image_saved")