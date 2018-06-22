from PIL import Image
img = Image.open("Sample.jpg")
img_info = img.info

print(img.format)
print( img.mode)
img.show()

image_file = img.convert('1') # convert image to black and white
image_file.save('result.png')

res = Image.open("result.png")
res.show()


img_rotate = img.rotate(90)
img_rotate.show()  # Displays the rotated image


w,h=img.size
n,m=[160,204]
cropped_img = img.crop((w//2 - n//2, h//2 - m//2, w//2 + n//2, h//2 + m//2))
cropped_img.show()

#thumbnail
img.thumbnail((75,75))
img.save("T_img.JPEG")
img.show()



