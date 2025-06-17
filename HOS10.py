from PIL import Image

def rotate_image(image_path, degrees):
    image = Image.open(image_path)
    rotated_image = image.rotate(degrees)
    rotated_image.save("rotated_image.jpg")
    print("Image rotated and saved as rotated_image.jpg")

rotate_image("/workspaces/hos10-spring-2025-NeekDaSneak-cityuseattle-hos10-spring-2025-NeekDaSneak/Groot.jpg", 90)