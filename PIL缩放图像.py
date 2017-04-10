import Image
im =Image.open('C:\Users\Administrator\Desktop\IMG_5076 (1).JPG')
w,h=im.size
im.thumbnail((w//2,h//2))
im.save('C:\Users\Administrator\Desktop\IMG_50762.JPG','jpeg')
