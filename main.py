from PIL import Image, ImageFont, ImageDraw
import csv

fontis = ImageFont.truetype('RAGE.ttf', 200)
imagelist = []
with open('data.csv', 'r') as data:
    read = csv.reader(data)
    for row in read:
        my_image = Image.open("baseimage.jpeg")
        name = row[0]
        institute = row[1]
        image_editable = ImageDraw.Draw(my_image)
        image_editable.text((15, 15), name, (237, 230, 211), font=fontis)
        image_editable.text((15, 500), institute, (237, 230, 211), font=fontis)
        my_image.convert('RGB')
        imagelist.append(my_image)
        my_image.save('certificates.pdf', save_all=True, append_images=imagelist)

