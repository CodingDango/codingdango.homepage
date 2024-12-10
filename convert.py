from PIL import Image

# img = Image.open('')

# img = img.convert('RGB')

# pixels = img.load()

# Open the image with transparency


png = Image.open('python.png').convert('RGBA')
background = Image.new('RGBA', png.size, (255,255,255))

alpha_composite = Image.alpha_composite(background, png)
alpha_composite.save('foo.png', 'PNG', quality=80)


# for i in range(img.size[0]):
#     for j in range(img.size[1]):
#         if pixels[i, j] == (0,0,0) or pixels[i, j] == (89,89,89):
#             pixels[i, j] = (255,255,255)
            
# img.save('modified_image.png')