import os
import random
from PIL import Image

def create_mosaic(target_image_path, input_images_path, output_image_path, grid_size):
    target_image = Image.open(target_image_path)
    input_images = []
    for file_name in os.listdir(input_images_path):
        with Image.open(os.path.join(input_images_path, file_name)) as img:
            input_images.append(img)
    grid_width = int(target_image.width / grid_size)
    grid_height = int(target_image.height / grid_size)
    output_image = Image.new('RGB', (target_image.width, target_image.height))
    for y in range(grid_height):
        for x in range(grid_width):
            target_grid = target_image.crop((x * grid_size, y * grid_size, (x + 1) * grid_size, (y + 1) * grid_size))
            input_image = random.choice(input_images).resize((grid_size, grid_size))
            output_image.paste(input_image, (x * grid_size, y * grid_size))
    output_image.save(output_image_path)

create_mosaic("picture.jpg", "p", "output.jpg", 50)